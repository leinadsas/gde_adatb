import sqlite3
import os




def GetConnection(db_name: str):
    
    """
    Létrehoz és visszaad egy SQLite adatbázis kapcsolatot
    A bemenet alapján dönt el, melyik adatbázist használja.
    """
    
    # Az a mappa ahol az adatbázisok találhatóak
    db_folder = "data"
    
    # A fájlnevet dinamikusan alakítjuk ki, kiterjesztéssel együtt
    db_file = os.path.join(db_folder, f"{db_name}.db")
    
    # A kapcsolat létrehozása
    conn = sqlite3.connect(db_file)
    return conn





    """
    Meghívása a következőképp:
    
    from database.connection import GetConnection
    
    conn = Getconnection("Adagok")
    """