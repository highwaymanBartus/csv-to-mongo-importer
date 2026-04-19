# Oficjalny obraz Pythona
FROM python:3.12

# Folder roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Domyślna komenda po uruchomieniu kontenera
CMD ["python", "main.py"]