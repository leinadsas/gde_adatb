from database.Connection import GetConnection
from database.Load_Csv import LoadCsv
import os
import pandas as pd
from datetime import datetime



def InserCoolSystemVersion2():
    
    conn = GetConnection("Kemence")
    cursor = conn.cursor()
    
    try:
        
        data_folder = "data"
        csv_path = os.path.join(data_folder, "Hűtőpanelek.csv")
        df_huto = LoadCsv(csv_path)

        # --- ÁTNEVEZŐ KÓDRÉSZ BESZÚRÁSA ITT! ---
  

        df_huto.rename(columns={
            'ï»¿Panel hÅ\x91fok 1 [Â°C] Time': 'date_time',
            'Panel hÅ\x91fok 1 [Â°C] ValueY': 'temp_1',
            'Panel hÅ\x91fok 2 [Â°C] ValueY': 'temp_2',
            'Panel hÅ\x91fok 3 [Â°C] ValueY': 'temp_3',
            'Panel hÅ\x91fok 4 [Â°C] ValueY': 'temp_4',
            'Panel hÅ\x91fok 5 [Â°C] ValueY': 'temp_5',
            'Panel hÅ\x91fok 6 [Â°C] ValueY': 'temp_6',
            'Panel hÅ\x91fok 8 [Â°C] ValueY': 'temp_8',
            'Panel hÅ\x91fok 9 [Â°C] ValueY': 'temp_9',
            'Panel hÅ\x91fok 10 [Â°C] ValueY': 'temp_10',
            'Panel hÅ\x91fok 11 [Â°C] ValueY': 'temp_11',
            'Panel hÅ\x91fok 12 [Â°C] ValueY': 'temp_12',
            'Panel hÅ\x91fok 13 [Â°C] ValueY': 'temp_13',
            'Panel hÅ\x91fok 14 [Â°C] ValueY': 'temp_14',
            'Panel hÅ\x91fok 15 [Â°C] ValueY': 'temp_15'

        
        }, inplace=True)

    
        nyers_huto_adatok_csv = df_huto.to_dict('records')

        print("Hűtőpanelek adatok sikeresen beolvasva és átnevezve.")

    except FileNotFoundError:
        print("Hiba: 'Hűtőpanelek.csv' nem található. Ellenőrizd az útvonalat!")
        exit()



    # 1. Lekérdezzük az összes olvasztás intervallumát az SQL táblából
    cursor.execute("SELECT ration_id, start_date_time, end_date_time FROM rations")


    olvasztas_intervallumok = cursor.fetchall()


    adatok_beszurasra = []

    # Dátum Formátum: Mivel a korábbi kódok szerint a dátumok így kerültek be az adatbázisba,
    # ezt használjuk a konverzióhoz.
    DATE_FORMAT = '%Y.%m.%d %H:%M:%S'

    # 2. Beolvassuk a Hűtőpanelek adatait (Nyers adatok)
    for sor in nyers_huto_adatok_csv:
        # A nyers mérési időpont
        meres_idopont_str = sor['date_time']

        # Konvertálás datetime objektummá
        try:
            # Feltételezzük, hogy az időpont a CSV-ben egyezik a DB-ben tárolt formátummal (de még TEXT)
            meres_dt = datetime.strptime(meres_idopont_str, DATE_FORMAT)
        except ValueError:
       
            continue

        # Keresd meg a megfelelő Olvasztas ID-t
        megtalalt_ration_id = None

        for r_id, start_dt_str, end_dt_str in olvasztas_intervallumok:
            # 3. Keresés: NULL Értékek és Konverzió
            if start_dt_str is None or end_dt_str is None:
                continue # Ugrás, ha az intervallum nem teljes

            try:
                # Konvertáljuk az SQL-ből érkező stringeket datetime objektummá
                start_dt = datetime.strptime(start_dt_str, DATE_FORMAT)
                end_dt = datetime.strptime(end_dt_str, DATE_FORMAT)
            except ValueError:
                continue 

            # ÖSSZEHASONLÍTÁS: Csak datetime objektumokat hasonlíthatunk össze!
            if start_dt <= meres_dt <= end_dt:
                megtalalt_ration_id = r_id
                break

        if megtalalt_ration_id:

            # --- Segéd-függvény a biztonságos konverzióhoz ---
            def safe_float_convert(value_str):
                if isinstance(value_str, str):
                    # Csak stringet kezel, cseréli a vesszőt pontra, majd konvertál.
                    return float(value_str.replace(',', '.'))
                return None  # Visszaadja a None-t, ha már nem string, vagy None volt


            try:
                beszurando_sor = (
                    megtalalt_ration_id,
                    meres_idopont_str,

                    # Konverzió az összes panelre:
                    safe_float_convert(sor['temp_1']),
                    safe_float_convert(sor['temp_2']),
                    safe_float_convert(sor['temp_3']),
                    safe_float_convert(sor['temp_4']),
                    safe_float_convert(sor['temp_5']),
                    safe_float_convert(sor['temp_6']),
                    safe_float_convert(sor['temp_8']),
                    safe_float_convert(sor['temp_9']),
                    safe_float_convert(sor['temp_10']),
                    safe_float_convert(sor['temp_11']),
                    safe_float_convert(sor['temp_12']),
                    safe_float_convert(sor['temp_13']),
                    safe_float_convert(sor['temp_14']),
                    safe_float_convert(sor['temp_15'])
                )
                adatok_beszurasra.append(beszurando_sor)

            except ValueError as e:
                print(f"Konverziós hiba (Vessző/Pont): {e}. Sor kihagyva.")
                continue

    # 5. Végleges Beszúrás az executemany-val
    cursor.executemany('''
        INSERT INTO cool_system (
            ration_id, 
            date_time, 
            temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, 
            temp_8, temp_9, temp_10, temp_11, temp_12, temp_13, temp_14, temp_15
    )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
    ''', adatok_beszurasra)

    conn.commit()