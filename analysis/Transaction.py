from database.Connection import GetConnection
import sqlite3


def Transaction():
    conn = GetConnection("Kemence")
    cursor = conn.cursor()
    
    try:
        # 1. Törli az Olvasztasok (rations) táblából a célsorokat.
        cursor.execute('''
                    DELETE FROM rations
                    WHERE ration_id NOT IN(
                        SELECT DISTINCT ration_id FROM cool_system
                    )
                    ''')
    
    
        conn.commit()
        print("\n\nAdattisztítás sikeresen véglegesítve.\n\n")
    
    except sqlite3.Error as e:
        # Hiba esetén visszagörgetés (ROLLBACK) a tranzakció elejére
        conn.rollback()
        print(f"\n\nHiba történt a tranzakció során: {e}. Visszagörgetés.\n\n")
    
    finally:
        conn.close()