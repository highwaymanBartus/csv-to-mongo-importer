from datetime import datetime, date
from typing import Any, Dict, List, Optional

from mapowanieKolumn import FLAT_FIELD_TYPES

#Braki danych:
EMPTY_VALUES = {"", "NULL", "NaN", None}

def isEmpty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str) and value.strip() in EMPTY_VALUES:
        return True
    return False

#Parsowanie:
def parseInt(value: str) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parseFloat(value: str) -> Optional[float]:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def parseBool(value: str) -> Optional[bool]:
    if not isinstance(value, str):
        return None

    val = value.strip().upper()
    if val == "TRUE":
        return True
    if val == "FALSE":
        return False

    return None

def parseDatetime(value: str) -> Optional[datetime]:
    try:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return None

def parseDate(value: str) -> Optional[datetime]:
    try:
        d = datetime.strptime(value, "%Y-%m-%d").date()  # parsowanie daty
        return datetime.combine(d, datetime.min.time())  # konwersja na datetime 00:00:00
    except (ValueError, TypeError):
        return None


#Transformacja pojedynczego pola:
def transformujPole(nazwa_pola: str, wartosc: Any, typDocelowy: Any) -> Any:
    if isEmpty(wartosc):
        return None

    if typDocelowy is None:
        return wartosc

    if typDocelowy is int:
        return parseInt(wartosc)

    if typDocelowy is float:
        return parseFloat(wartosc)

    if typDocelowy is bool:
        return parseBool(wartosc)

    if typDocelowy is datetime:
        wynik = parseDatetime(wartosc)
        if wynik is None:
            wynik = parseDate(wartosc)
        return wynik

    if typDocelowy is date:
        return parseDate(wartosc)

    # Fallback, jak doleci tutaj to zostawiamy bez zmian:
    return wartosc


# Rekurencyjna transformacja struktury:
def transformujStrukture(dane: Dict[str, Any], typyDanych: Dict[str, Any], sciezka: str = "") -> Dict[str, Any]:
    wynik = {}

    for klucz, wartosc in dane.items():
        aktualnaSciezka = f"{sciezka}.{klucz}" if sciezka else klucz

        if isinstance(wartosc, dict):
            if klucz == "_external":
                wynik[klucz] = wartosc
            else:
                wynik[klucz] = transformujStrukture(wartosc, typyDanych, aktualnaSciezka)
        else:
            typDocelowy = typyDanych.get(aktualnaSciezka)
            wynik[klucz] = transformujPole(aktualnaSciezka, wartosc, typDocelowy)
            
    return wynik


#Publiczne API modułu:
def transformujRekord(zmapowanyRekord: Dict[str, Any]) -> Dict[str, Any]:
    return transformujStrukture(zmapowanyRekord, FLAT_FIELD_TYPES)

def transformujWiele(rekordy: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [transformujRekord(r) for r in rekordy]