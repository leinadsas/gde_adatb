import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

# 1. TISZTÍTÁS: Töröld a régi táblákat, ha léteznek!
#    FONTOS: A cool_system-et kell előbb törölni, mert hivatkozik a rations-ra (FK miatt)!
cursor.execute("DROP TABLE IF EXISTS cool_system;")
cursor.execute("DROP TABLE IF EXISTS rations;")

# 2. CREATE RATIONS (Szülő tábla létrehozása)
cursor.execute('''
               CREATE TABLE rations
               (
                   ration_id       INTEGER PRIMARY KEY,
                   start_date_time Text,
                   end_date_time   Text
               )
               ''')

# 3. CREATE COOL_SYSTEM (Gyermek tábla létrehozása FK-val)
cursor.execute('''
               CREATE TABLE cool_system
               (
                   id        INTEGER PRIMARY KEY AUTOINCREMENT,
                   ration_id INTEGER NOT NULL,
                   date_time Text,
                   temp_1 REAL,
                   temp_2 REAL,
                   temp_3 REAL,
                   temp_4 REAL,
                   temp_5 REAL,
                   temp_6 REAL,
                   temp_8 REAL,
                   temp_9 REAL,
                   temp_10 REAL,
                   temp_11 REAL,
                   temp_12 REAL,
                   temp_13 REAL,
                   temp_14 REAL,
                   temp_15 REAL,

                   FOREIGN KEY (ration_id) REFERENCES rations (ration_id)
               )
               ''')

conn.commit()
conn.close()