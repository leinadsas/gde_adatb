from database.Connection import GetConnection



def InsertRations():
    conn = GetConnection("Kemence")
    cur = conn.cursor()

    # A táblaneveket át kell nevezni, és és az új oszlopnevekkel táblát kell rendezni

    cur.execute("DROP TABLE IF EXISTS adagok_rendezett;")

    # Rendezett nézet létrehozása
    cur.execute("""
                CREATE TABLE adagok_rendezett AS
                SELECT
                    [ADAGSZµM]    AS adag_szam,
                    [Kezdet_DµTUM] AS kezdet_datum, 
                    [Kezdet_ID\x8a]   AS kezdet_ido,        -- Itt a 3-4-5 Máshogy olvassa be a fordító mint ahogy a csv fájlban van, így azt kell odaírni,
                    [V\x82ge_DµTUM]   AS vege_datum,        -- amit a debugging során a változó értéket felvesz
                    [V\x82ge_ID\x8a]     AS vege_ido
                FROM adagok;
                """)

    # Adatok feltöltése a rations táblába
    cur.execute("""
                INSERT INTO rations (ration_id, start_date_time, end_date_time)
                SELECT
                    adag_szam,
                    kezdet_datum || ' ' || kezdet_ido AS start_date_time,
                    vege_datum || ' ' || vege_ido AS end_date_time
                FROM adagok_rendezett;
                """)
    
    print(f"Sikeresen átmásolva: {cur.rowcount} sor \n\n")
    
    conn.commit()
    conn.close()