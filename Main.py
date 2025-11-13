from database.Create_tables import CreateTables
from database.Load_adagok import LoadAdagok
from database.Load_hutopanel import LoadHutopanel
from database.Insert_rations import InsertRations
from database.Insert_cool_system_version2 import InserCoolSystemVersion2
from database.Create_index import CreateIndex
from cleaning.ClearTerminal import clear_terminal
from analysis.Transaction import Transaction

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
    InserCoolSystemVersion2()
    
    print("=== Indexelés ===")
    CreateIndex()
    
    print("=== Tranzakció futtatása ===")
    Transaction()
    
    
    
if __name__ == "__main__":
    Main()