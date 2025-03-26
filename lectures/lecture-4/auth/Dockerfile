# Używamy obrazu Pythona
FROM python:3.11

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki i instalujemy zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę kodu
COPY . .

# Uruchamiamy aplikację
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
