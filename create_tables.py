import sqlite3

# connect to SQL data base

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

# create cool_system table
cursor.execute('''
    CREATE TABLE cool_system(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time Text,
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
    temp_15 REAL)
        ''')

# create rations data base
cursor.execute('''
CREATE TABLE rations(
ration_id INTEGER PRIMARY KEY AUTOINCREMENT,
start_date_time Text,
end_date_time Text)
''')

conn.commit()
conn.close()





