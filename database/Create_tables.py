from database.Connection import GetConnection

def CreateTables():
    conn = GetConnection("Hűtőpanel_adatbázis")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rations (
            ration_id INTEGER PRIMARY KEY AUTOINCREMENT,
            panel_id INTEGER NOT NULL,
            start_date_time TEXT NOT NULL,
            end_date_time TEXT NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS cool_system (
            panel_id INTEGER NOT NULL,
            date_time TEXT PRIMARY KEY,
            temp_1 REAL, temp_2 REAL, temp_3 REAL, temp_4 REAL, temp_5 REAL,
            temp_6 REAL, temp_7 REAL, temp_8 REAL, temp_9 REAL, temp_10 REAL, temp_11 REAL,
            temp_12 REAL, temp_13 REAL, temp_14 REAL, temp_15 REAL,
            FOREIGN KEY (panel_id) REFERENCES rations(panel_id)
        );
    """)

    # teljesítmény (JOIN-okra) – opcionális index
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rations_panel ON rations(panel_id);")

    conn.commit()
    conn.close()
    print("Hűtőpanel_adatbázis: rations és cool_system létrehozva.")