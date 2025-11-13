import pandas as pd
import os


# Külön egy .csv fájlkiterjesztésű betöltő mivel két helyen is kell használni ugyanazt a funkciót hibakereséssel, 
# így több értelme van külön használni modulárisan.

def LoadCsv(path: str) -> pd.DataFrame:
    """
    Betölti a megadott CSV fájlokat
    - Adagok.csv
    - Hűtőpanelek.csv
    """
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Nem található a fájl: {path}")
    
    
    return pd.read_csv(path, sep=";", encoding = "latin-1")