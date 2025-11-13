from database.Create_tables import CreateTables
from database.Load_adagok import LoadAdagok
from database.Load_hutopanel import LoadHutopanel
from database.Insert_rations import InsertRations
from database.Insert_cool_system import InsertCoolSystem
from cleaning.ClearTerminal import clear_terminal

def Main():
    
    clear_terminal()
    
    print("=== Táblák létrehozása ===")
    CreateTables()
    
    print("=== Adagok betöltése ===")
    LoadAdagok()
    
    print("=== Hűtőpanelek betöltése ===")
    LoadHutopanel()
    
    print("=== Rations feltöltése ===")
    InsertRations()
    
    print("=== Cool system feltöltése ===")
    InsertCoolSystem()
    
    
    
if __name__ == "__main__":
    Main()