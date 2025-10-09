import pandas as pd
import sqlite3

conn = sqlite3.connect('Kemence.sql')
cursor = conn.cursor()

# Adagok CSV read, a szeparátort be kell állítani a helyes beolvasás miatt
df = pd.read_csv('Adagok.csv', encoding='latin-1', sep=';')

# data write to SQL
df.to_sql('adagok', conn, if_exists='replace', index=False )
print("Sikeres feltöltés!")
print(f"Beolvasott sorok: {len(df)}")
print(f"Oszlopok: {df.columns.tolist()}")

conn.close()
