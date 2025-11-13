from database.Connection import GetConnection



def InsertCoolSystem():
    
    conn = GetConnection("Kemence")
    cur = conn.cursor()
    
    # Külső kulcsok bekapcsolása
    cur.execute("PRAGMA foreign_keys = ON;")
    
    # Ideiglenes oszlopnevű tábla
    cur.execute("DROP TABLE IF EXISTS hutopanelek_rendezett;")
    cur.execute("""
                CREATE TABLE hutopanelek_rendezett AS
                SELECT
                    "ï»¿Panel hÅfok 1 [Â°C] Time"    AS date_time,
                    "Panel hÅfok 1 [Â°C] ValueY"    AS temp_1,
                    "Panel hÅfok 2 [Â°C] ValueY"    AS temp_2,
                    "Panel hÅfok 3 [Â°C] ValueY"    AS temp_3,
                    "Panel hÅfok 4 [Â°C] ValueY"    AS temp_4,
                    "Panel hÅfok 5 [Â°C] ValueY"    AS temp_5,
                    "Panel hÅfok 6 [Â°C] ValueY"    AS temp_6,
                    NULL                             AS temp_7,        -- Nincs 7-es panel!
                    "Panel hÅfok 8 [Â°C] ValueY"    AS temp_8,
                    "Panel hÅfok 9 [Â°C] ValueY"    AS temp_9,
                    "Panel hÅfok 10 [Â°C] ValueY"   AS temp_10,
                    "Panel hÅfok 11 [Â°C] ValueY"   AS temp_11,
                    "Panel hÅfok 12 [Â°C] ValueY"   AS temp_12,
                    "Panel hÅfok 13 [Â°C] ValueY"   AS temp_13,
                    "Panel hÅfok 14 [Â°C] ValueY"   AS temp_14,
                    "Panel hÅfok 15 [Â°C] ValueY"   AS temp_15
                FROM hutopanelek;
                """)
    
    # Átmásolás a végleges táblába
    cur.execute("""
                INSERT INTO cool_system (
                    ration_id, date_time,
                    temp_1, 
                    temp_2, 
                    temp_3, 
                    temp_4, 
                    temp_5,
                    temp_6, 
                    temp_7, 
                    temp_8, 
                    temp_9, 
                    temp_10,
                    temp_11, 
                    temp_12, 
                    temp_13, 
                    temp_14, 
                    temp_15
                )
                SELECT
                    1 AS ration_id,
                    date_time,
                    temp_1, 
                    temp_2, 
                    temp_3, 
                    temp_4, 
                    temp_5,
                    temp_6, 
                    temp_7, 
                    temp_8, 
                    temp_9, 
                    temp_10,
                    temp_11, 
                    temp_12, 
                    temp_13, 
                    temp_14, 
                    temp_15
                FROM hutopanelek_rendezett
                """)
    
    print(f"Sikeresen átmásolva: {cur.rowcount} sor \n\n")
    conn.commit()
    conn.close()
    