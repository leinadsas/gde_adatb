import sqlite3
import sys
from database.Connection import GetConnection

def create_index():
    """
    Létrehozza a 'date_time' oszlopra az indexet a 'cool_system' táblán.
    """
    try:
        # Csatlakozás az adatbázishoz
        conn_huto = GetConnection("Hűtőpanelek")
        cur = conn_huto.cursor()
        
        # Az SQL parancs - érdemes IF NOT EXISTS-et használni,
        # hogy ne kapj hibát, ha már létezik.
        sql_command = """
        CREATE INDEX IF NOT EXISTS idx_date_time 
        ON cool_system (date_time ASC);
        """
        
        # Parancs végrehajtása
        cur.execute(sql_command)
        
        # Kommitálás (CREATE INDEX esetén implicit lehet, de nem árt)
        conn_huto.commit()
        
        print("Az 'idx_date_time' index sikeresen létrehozva.")
        
    except sqlite3.Error as e:
        print(f"Hiba történt az index létrehozása közben: {e}", file=sys.stderr)
        
    finally:
        # Kapcsolat bezárása
        if conn_huto:
            conn_huto.close()

# Ez a rész biztosítja, hogy a create_index() csak akkor fusson le,
# ha magát a create_index.py fájlt futtatod közvetlenül.
if __name__ == "__main__":
    create_index()