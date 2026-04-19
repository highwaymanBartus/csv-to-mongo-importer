## csv-to-mongo-importer
Projekt zaliczeniowy polegający na implementacji pipeline’u ETL (Extract–Transform–Load) służącego do przetwarzania danych autorskiego badania naukowego zapisanych w formacie CSV oraz ich zapisu do bazy danych MongoDB.

Dane wejściowe (CSV) posiadają płaską strukturę, brak typowania oraz niespójne formaty (np. daty, wartości logiczne). W ramach projektu zostało zaimplementowane:

- wczytywanie i parsowanie danych z pliku CSV
- mapowanie kolumn CSV do wewnętrznej, zagnieżdżonej struktury dokumentów
- transformacja typów danych (string → int, float, bool, datetime)
- obsługa brakujących i niepoprawnych wartości
- budowa ustrukturyzowanych dokumentów zgodnych z modelem MongoDB
- zapis danych do bazy w trybie upsert (zapobieganie duplikatom i aktualizacja rekordów)
- możliwość wykonywania zapytań analitycznych na danych po imporcie

Całość została uruchomiona w środowisku kontenerowym (Docker), co zapewnia powtarzalność oraz izolację środowiska wykonawczego.

## Technologie
- Python
- PyMongo
- Docker
- Docker Compose
- MongoDB

## Czego się nauczyłem
- wczytywania danych z CSV
- transformacji i parsowania typów
- organizacji pipeline'u
- komunikacji z bazą danych (pymongo.MongoClient)
- przechowywania przetworzonych danych z badania
- obsługi zagnieżdżonych struktur (.raw, .summary)
- izolacji środowiska uruchomieniowego
- jednoczesnego uruchamiania aplikacji Python i bazy MongoDB (przy użyciu Docker Comnpose)
