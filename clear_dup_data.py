import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

# Másik megközelítés
cursor.execute('''
    DELETE FROM cool_system 
    WHERE rowid IN (
        SELECT rowid FROM (
            SELECT rowid, 
                   ROW_NUMBER() OVER (PARTITION BY date_time ORDER BY rowid) as rn
            FROM cool_system
        ) WHERE rn > 1
    );
''')

# Ellenőrizzük, hány sor törlődött
print(f"{cursor.rowcount} sor törölve")

conn.commit()
conn.close()
