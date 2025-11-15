import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

try:
    
    cursor.execute('BEGIN TRANSACTION; ')

    # Megnézzük, mely ration_id-k fognak törlődni
    cursor.execute('''
    SELECT ration_id 
    FROM rations 
    WHERE ration_id NOT IN (SELECT DISTINCT ration_id FROM cool_system)
    ORDER BY ration_id;''')

    # 1. Törli az Olvasztasok (rations) táblából a célsorokat.

    cursor.execute('''
    DELETE FROM rations
    WHERE ration_id NOT IN (
                            SELECT DISTINCT ration_id 
                            FROM cool_system);''')


    conn.commit()
    print("Adattisztítás sikeresen véglegesítve.")

except sqlite3.Error as e:
    # Hiba esetén visszagörgetés (ROLLBACK) a tranzakció elejére
    conn.rollback()
    print(f"Hiba történt a tranzakció során: {e}. Visszagörgetés.")

finally:
    conn.close()