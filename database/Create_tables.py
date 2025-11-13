from database.Connection import GetConnection
import sqlite3

def CreateTables():
    conn = GetConnection("Kemence")
    cur = conn.cursor()
    
    # Ha léteznek már ilyen táblák akkor azükat töröljük
    cur.execute("DROP TABLE IF EXISTS rations;")
    cur.execute("DROP TABLE IF EXISTS cool_system;")
    
    # Táblák létrehozása
    cur.execute("""
        CREATE TABLE rations (
            ration_id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date_time,
            end_date_time
        );
    """)

    cur.execute("""
        CREATE TABLE cool_system (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            ration_id INTEGER NOT NULL,
            date_time TEXT,
            temp_1 REAL, 
            temp_2 REAL, 
            temp_3 REAL, 
            temp_4 REAL, 
            temp_5 REAL,
            temp_6 REAL, 
            temp_7 REAL, 
            temp_8 REAL, 
            temp_9 REAL, 
            temp_10 REAL, 
            temp_11 REAL,
            temp_12 REAL, 
            temp_13 REAL, 
            temp_14 REAL, 
            temp_15 REAL,
            FOREIGN KEY (ration_id) REFERENCES rations (ration_id)
        );
    """)

    conn.commit()
    conn.close()
    print("Hűtőpanel_adatbázis: rations és cool_system létrehozva. \n\n")