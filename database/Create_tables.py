from database.Conection import GetConnection




def CreateTables():
    """
    Létrehozza a szükséges táblákat az ER-diagram alapján, az Adagok és Hűtőpanelek adatbázisokban.
    """
    
    # 1. Adagok (rations) adatbázis létrehozása
    conn_adagok = GetConnection("Adagok")
    cur1 = conn_adagok.cursor()
    
    cur1.execute("""
        CREATE TABLE IF NOT EXISTS rations (
            ration_id INTEGER RIMARY KEY AUTOINCREMENT,
            panel_id INTEGER NOT NULL,
            start_date_time TEXT NOT NULL,
            end_date_time TEXT NOT NULL
        );
    """)
    
    conn_adagok.commit()
    conn_adagok.close()
    
    
    # 2. Hűtőpanelek (cool_system) adatbázis létrehozása
    conn_huto = GetConnection("Hűtőpanelek")
    cur2 = conn_huto.cursor()
    
    cur2.execute("""
        CREATE TABLE IF NOT EXISTS cool_system (
            date_time TEXT PRIMARY KEY,
            temp_1 REAL, temp_2 REAL, temp_3 REAL, temp_4 REAL, temp_5 REAL,
            temp_6 REAL, temp_7 REAL, temp_8 REAL, temp_9 REAL, temp_10 REAL, temp_11 REAL,
            temp_12 REAL, temp_13 REAL, temp_14 REAL, temp_15 REAL
        );
    """)
    
    conn_huto.commit()
    conn_huto.close()
    
    print("Adatbázis táblák sikeresen létrehozva.")
    