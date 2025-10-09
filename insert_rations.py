
import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()
# A táblanevek nem megfelelőek ezért át kell nevezni
#  Új oszlopnevekkel tábla rendezése
cursor.execute('''
    CREATE TABLE IF NOT EXISTS adagok AS
    SELECT 
        "ADAGSZµM" as adag_szam,
        "Kezdet_DµTUM" as kezdet_datum, 
        "Kezdet_ID" as kezdet_ido,
        "Vge_DµTUM" as vege_datum,
        "Vge_ID" as vege_ido,
    FROM adagok
''')

# 2. Adatok feltöltése
cursor.execute('''
    INSERT INTO rations (ration_id, start_date_time, end_date_time)
    SELECT 
        adag_szam,
        kezdet_datum || ' ' || kezdet_ido AS start_date_time,
        vege_datum || ' ' || vege_ido AS end_date_time
    FROM adagok
''')

print(f"Sikeresen átmásolva: {cursor.rowcount} sor")
conn.commit()
conn.close()