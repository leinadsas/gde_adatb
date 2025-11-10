from database.Connection import GetConnection
import pandas as pd
import os
import chardet


def InsertData():
    """
    Beolvassa az Adagok.csv és Hűtőpanelek.csv fájlokat a /data mappából,
    majd feltölti őket a Hűtőpanel_adatbázis.db adatbázis két táblájába:
      - rations(start_date_time, end_date_time)
      - cool_system(panel_id, date_time, temp_1..temp_15)
    Feltételezés: a táblák már léteznek (Create_tables.CreateTables futott).
    """

    # 1. Fájlok elérési útja
    
    data_folder = "data"
    adagok_path = os.path.join(data_folder, "Adagok.csv")
    hutopanelek_path = os.path.join(data_folder, "Hűtőpanelek.csv")

    # 2. CSV fájlok beolvasása
    
    df_adagok = LoadCsv(adagok_path)
    df_huto = LoadCsv(hutopanelek_path)
    
    # 3. Adagok: konkrét átnevezés + összevonás
    df_adagok = df_adagok.rename(columns={
        "ADAGSZÁM":   "panel_id",
        "Kezdet_DÁTUM": "start_d",
        "Kezdet_IDŐ":   "start_t",
        "Vége_DÁTUM":   "end_d",
        "Vége_IDŐ":     "end_t",
    })
    df_adagok["start_date_time"] = df_adagok["start_d"].astype(str).str.strip() + " " + df_adagok["start_t"].astype(str).str.strip()
    df_adagok["end_date_time"]   = df_adagok["end_d"].astype(str).str.strip()   + " " + df_adagok["end_t"].astype(str).str.strip()
    df_adagok = df_adagok[["panel_id", "start_date_time", "end_date_time"]].copy()
    
    # 4. Hűtőpanelek: idő + hőfokok átnevezése
    df_huto = df_huto.rename(columns={"Time": "date_time"})
    for i in range(1, 16):
        hu = f"Panel hőfok {i} [°C]"
        if hu in df_huto.columns:
            df_huto = df_huto.rename(columns={hu: f"temp_{i}"})
    needed = ["panel_id", "date_time"] + [f"temp_{i}" for i in range(1, 16)]
    df_huto = df_huto[needed].copy()
    
    # 4) Sorok előkészítése (egyszerű, pozíciós tuple)
    def to_int(x):
        try: return int(float(str(x).replace(",", ".").strip()))
        except: return None
    def to_float(x):
        try:
            s = str(x).strip().replace(",", ".")
            return float(s) if s else None
        except: return None
    
    rows_rations = [
        (to_int(p), str(s), str(e))
        for (p, s, e) in df_adagok.itertuples(index=False, name=None)
        if to_int(p) is not None
    ]
    rows_cool = []
    for row in df_huto.itertuples(index=False, name=None):
        p, dt, *temps = row
        rows_cool.append((to_int(p), str(dt)) + tuple(to_float(x) for x in temps))
    
    
    # 5. Két tábla feltöltése egyetlen kapcsolattal
    conn = GetConnection("Hűtőpanel_adatbázis")
    try:
        cur = conn.cursor()
        # Külső kulcsok ellenőrzésének bekapcsolása    (mert az SQLite automatikusan ezt nem ellenőrzi így ezzel az összefüggés sértés elkerülhető)
        cur.execute("PRAGMA foreign_keys = ON;")

        # rations insert (executemany gyors)
        cur.executemany(
            "INSERT INTO rations (panel_id, start_date_time, end_date_time) VALUES (?, ?, ?);",
            rows_rations
        )

        # cool_system insert – date_time PRIMARY KEY, duplikátumokat ignoráljuk
        cur.executemany(
            """
            INSERT OR IGNORE INTO cool_system (
                panel_id, date_time,
                temp_1, temp_2, temp_3, temp_4, temp_5,
                temp_6, temp_7, temp_8, temp_9, temp_10, temp_11,
                temp_12, temp_13, temp_14, temp_15
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            rows_cool
        )
        
        conn.commit()
        # a duplikátumok ignorálásával kiírja hány sor lett feltöltve az adatbázisba
        print(f"Feltöltve: rations={len(rows_rations)} sor, cool_system={len(rows_cool)} sor (duplikátumok ignorálva).")
    finally:
        conn.close()




# Külön egy .csv fájlkiterjesztésű betöltő mivel két helyen is kell használni ugyanazt a funkciót hibakereséssel így több értelme van külön használni modulárisan

def LoadCsv(path: str) -> pd.DataFrame:
    """
    Betölti a megadott CSV fájlt a megfelelő kódolással.
    - Adagok.csv → CP852 (DOS Central Europe)
    - Hűtőpanelek.csv → UTF-8 BOM (utf-8-sig)
    - Minden más esetben → alapértelmezett UTF-8 BOM
    """
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Nem található a fájl: {path}")
    
    name = os.path.basename(path).lower()
    
    # Kódolás automatikus detektálása
    with open(path, 'rb') as f:
        raw_data = f.read(2048)  # első 2 KB elég a mintához
    result = chardet.detect(raw_data)
    detected_enc = result.get("encoding", "")
    confidence = result.get("confidence", 0)
    
    try:
        if detected_enc and confidence >= 0.6:
            return pd.read_csv(path, sep=";", encoding=detected_enc)
    except Exception:
        pass
    
    # Hűtőpanelek: UTF-8 BOM + pontosvessző
    if "hűtő" in name or "huto" in name:
        return pd.read_csv(path, sep=";", encoding="utf-8-sig")

    # Alapértelmezett fallback (ritkán kell)
    else:
        return pd.read_csv(path, sep=";", encoding="utf-8-sig")