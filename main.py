import os

from wczytywanieCSV import wczytajCSV, mapujKolumny
from mapowanieKolumn import COLUMN_MAP
from transformowanieCSV import transformujWiele
from zapisMongo import connectMongo, upsertRecords

def main():
    sciezkaCSV = "AR.csv"
    suroweDane = wczytajCSV(sciezkaCSV)
    print(f"Wczytano {len(suroweDane)} wierszy surowych danych.")

    zmapowaneDane = mapujKolumny(suroweDane, COLUMN_MAP)
    #print(f"Zmapowano kolumny, przykładowy wiersz:")
    #print(zmapowaneDane[14] if zmapowaneDane else "Brak danych (zawiodło mapowanie)")

    przeksztalconeDane = transformujWiele(zmapowaneDane)
    #print(f"Przekształcono typy danych, przykładowy wiersz:")
    #print(przeksztalconeDane[14] if przeksztalconeDane else "Brak danych (zawiodło przekształcanie)")

    print("\nŁączenie z MongoDB...")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
    DB_NAME = "AR_study"
    COLLECTION = "dane"
    baza = connectMongo(MONGO_URI, DB_NAME)
    
    print("Zapisywanie rekordów do kolekcji 'dane' (upsert)...")
    upsertRecords(baza, COLLECTION, przeksztalconeDane, "id.meta.value")
    print("Zapis zakończony.")
    
    print("Sanity check:")
    for i, rekord in enumerate(przeksztalconeDane[:5]):
        print(f"Rekord {i+1}: {rekord}")

if __name__ == "__main__":
    main()
