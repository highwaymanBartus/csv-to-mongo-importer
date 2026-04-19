# zapisMongo.py
from pymongo import MongoClient
from typing import List, Dict, Optional

# Prywatna zmienna przechowująca klienta Mongo – nie trzeba jej przekazywać w każdej funkcji
_client: Optional[MongoClient] = None


def connectMongo(uri: str, nazwaBazy: str):
    """
    Nawiązuje połączenie z MongoDB i zwraca obiekt bazy danych.
    
    :param uri: adres serwera Mongo, np. "mongodb://localhost:27017"
    :param db_name: nazwa bazy danych
    :return: obiekt bazy danych
    """
    global _client
    _client = MongoClient(uri)
    bazaDanych = _client[nazwaBazy]
    return bazaDanych


def insertRecords(bazaDanych, collectionName: str, records: List[Dict]):
    """
    Wstawia listę rekordów do danej kolekcji.
    
    :param db: obiekt bazy danych zwrócony przez connect_mongo
    :param collection_name: nazwa kolekcji
    :param records: lista słowników do wstawienia
    :return: lista ID wstawionych rekordów
    """
    if _client is None:
        raise RuntimeError("Nie podłączono do Mongo. Błąd funkcji: insertRecords - wywołaj connect_mongo() najpierw.")
    
    collection = bazaDanych[collectionName]
    result = collection.insert_many(records)
    return result.inserted_ids

def get_nested(record, path):
    keys = path.split(".")
    val = record
    for k in keys:
        if not isinstance(val, dict):
            return None
        val = val.get(k)
    return val

def upsertRecords(bazaDanych, collectionName: str, records: List[Dict], keyField: str):
    """
    Wstawia lub aktualizuje rekordy na podstawie klucza unikalnego.
    Jeśli rekord o tym samym key_field już istnieje, zostaje nadpisany.
    
    :param db: obiekt bazy danych
    :param collection_name: nazwa kolekcji
    :param records: lista słowników do wstawienia lub aktualizacji
    :param key_field: nazwa pola używanego jako unikalny klucz (np. "id")
    """
    if _client is None:
        raise RuntimeError("Nie podłączono do Mongo. Błąd funkcji: upsertRecords - wywołaj connect_mongo() najpierw.")
    
    collection = bazaDanych[collectionName]
    
    for record in records:
        key_value = get_nested(record, keyField)
        if key_value is None:
            continue

        collection.update_one(
            {keyField: key_value},
            {"$set": record},
            upsert=True
)
