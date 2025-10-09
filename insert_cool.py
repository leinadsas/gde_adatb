import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

# 1. Új tábla létrehozása egyszerűbb oszlopnevekkel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hutopanelek_norm AS
    SELECT 
        "ï»¿Panel hÅfok 1 [Â°C] Time" as date_time,
        "Panel hÅfok 1 [Â°C] ValueY" as temp_1, 
        "Panel hÅfok 2 [Â°C] ValueY" as temp_2, 
        "Panel hÅfok 3 [Â°C] ValueY" as temp_3,
        "Panel hÅfok 4 [Â°C] ValueY" as temp_4,
        "Panel hÅfok 5 [Â°C] ValueY" as temp_5,
        "Panel hÅfok 6 [Â°C] ValueY" as temp_6, 
        "Panel hÅfok 7 [Â°C] ValueY" as temp_7, 
        "Panel hÅfok 8 [Â°C] ValueY" as temp_8,
        "Panel hÅfok 9 [Â°C] ValueY" as temp_9,
        "Panel hÅfok 10 [Â°C] ValueY" as temp_10,
        "Panel hÅfok 11 [Â°C] ValueY" as temp_11, 
        "Panel hÅfok 12 [Â°C] ValueY" as temp_12, 
        "Panel hÅfok 13 [Â°C] ValueY" as temp_13,
        "Panel hÅfok 14 [Â°C] ValueY" as temp_14,
        "Panel hÅfok 15 [Â°C] ValueY" as temp_15    -- ← NINCS VESSŐ A VÉGÉN!
    FROM hutopanelek
''')

# 2. Adatok feltöltése
cursor.execute('''
    INSERT INTO cool_system (date_time, temp_1, temp_2, temp_3, temp_4, temp_5, 
                           temp_6, temp_7, temp_8, temp_9, temp_10, 
                           temp_11, temp_12, temp_13, temp_14, temp_15)
    SELECT 
        date_time,
        temp_1,    -- ← temp_1 is kell!
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
    FROM hutopanelek_norm
''')

print(f"Sikeresen átmásolva: {cursor.rowcount} sor")
conn.commit()
conn.close()