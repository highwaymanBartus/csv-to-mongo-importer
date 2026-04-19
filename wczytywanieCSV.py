# wczytywanieCSV.py
import csv
from typing import List, Dict

from mapowanieKolumn import COLUMN_MAP

def wczytajCSV(sciezka: str, delimiter: str = ',', encoding: str = 'utf-8') -> List[Dict[str, str]]:
    wiersze = []
    
    with open(sciezka, mode='r', encoding=encoding, newline='') as plikCSV:
        czytnik = csv.DictReader(plikCSV, delimiter=delimiter)
        for wiersz in czytnik:
            wiersze.append(wiersz)
    
    return wiersze

def mapujKolumny(wiersze: List[Dict[str, str]], column_map: Dict) -> List[Dict]:
    """
    Mapuje nagłówki CSV na wewnętrzną strukturę projektu według COLUMN_MAP.
    
    :param wiersze: lista słowników wczytanych z CSV
    :param column_map: słownik mapowania kolumn (COLUMN_MAP)
    :return: lista słowników z nazwami zgodnymi z mapowaniem
    """
    zmapowaneWiersze = []

    for wiersz in wiersze:  #Dla każdego nowego badanego tworzymy...
        nowyWiersz = {}     #...nowy pusty słownik nowyWiersz
        for sekcja, sekcja_map in column_map.items():
            nowyWiersz[sekcja] = {}
            for podsekcja, kolumny in sekcja_map.items():
                nowyWiersz[sekcja][podsekcja] = {}
                for nazwaWew, nazwa_csv in kolumny.items():
                    nowyWiersz[sekcja][podsekcja][nazwaWew] = wiersz.get(nazwa_csv, None)
        zmapowaneWiersze.append(nowyWiersz)

    return zmapowaneWiersze