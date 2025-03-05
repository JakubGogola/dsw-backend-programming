# Używamy obrazu Python 3.10
FROM python:3.10-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik requirements.txt i instalujemy zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy wszystkie pliki aplikacji
COPY . .

# Uruchamiamy aplikację za pomocą Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
