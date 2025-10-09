import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

cursor.execute('''
            INSERT INTO rations (ration_id, start_date_time, end_date_time)
            SELECT 
                ADAGSZµM,
                Kezdet_DµTUM || ' ' || Kezdet_ID AS start_date_time,
                V ge_DµTUM || ' ' || V ge_ID AS end_date_time
            FROM adagok
            ''')

conn.commit()
conn.close()