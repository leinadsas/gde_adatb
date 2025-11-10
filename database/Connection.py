import sqlite3
import os




def GetConnection(db_name: str):
    
    """
    Létrehoz és visszaad egy SQLite adatbázis kapcsolatot
    A bemenet alapján dönti el, melyik adatbázist használja.
    """
    
    # A 'database' mappában vagyunk -> feljebb lépünk a projekt gyökérig,
    # majd ott használjuk a 'data' mappát abszolút úttal.
    # Az a mappa ahol az adatbázisok találhatóak
    
    project_root = os.path.dirname(os.path.dirname(__file__))
    db_folder = os.path.join(project_root, "data")
    os.makedirs(db_folder, exist_ok=True)  # ha nincs, létrehozza
    
    # A fájlnevet dinamikusan alakítjuk ki, kiterjesztéssel együtt
    db_file = os.path.join(db_folder, f"{db_name}.db")
    
    print(f"[GetConnection] DB path: {db_file}")
    
    # A kapcsolat létrehozása
    conn = sqlite3.connect(db_file)
    return conn





    """
    Meghívása a következőképp:
    
    from database.connection import GetConnection
    
    conn = Getconnection("Adagok")
    """