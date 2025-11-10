import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

try:
    # 1. Törli az Olvasztasok (rations) táblából a célsorokat.
    cursor.execute('''
                   DELETE
                   FROM rations
                   WHERE ration_id < 14;
                   ''')


    conn.commit()
    print("Adattisztítás sikeresen véglegesítve.")

except sqlite3.Error as e:
    # Hiba esetén visszagörgetés (ROLLBACK) a tranzakció elejére
    conn.rollback()
    print(f"Hiba történt a tranzakció során: {e}. Visszagörgetés.")

finally:
    conn.close()