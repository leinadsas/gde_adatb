from database.Create_tables import CreateTables
from database.Insert_data import InsertData  # a CSV-s verzió, amit együtt raktunk össze

def Main():
    
    # 1) Táblák létrehozása
    CreateTables()

    # 2) Adatok betöltése a már létező táblákba
    InsertData()
    
if __name__ == "__main__":
    Main()