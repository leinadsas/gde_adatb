from database.Connection import GetConnection
from database.Load_Csv import LoadCsv
import os
import pandas as pd
import sqlite3

def LoadAdagok():
    conn = GetConnection("Kemence")

    # Adagok beolvasása, LoadCsv függvénnyel

    data_folder = "data"
    csv_path = os.path.join(data_folder, "Adagok.csv")
    df = LoadCsv(csv_path)


    # Adatbeírás SQL-be

    df.to_sql('adagok', conn, if_exists='replace', index = False)
    print("Sikeres feltöltés!")
    print(f"Beolvasott sorok: {len(df)}")
    print(f"Oszlopok: {df.columns.tolist()} \n\n")

    conn.close()
