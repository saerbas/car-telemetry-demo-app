# Wir nutzen ein "Slim" Image, damit der Container nicht 1GB groß wird
# Python 3.9 oder 3.10 ist super stabil für Pandas
FROM python:3.10-slim

WORKDIR /app

# WICHTIG: Erst requirements kopieren und installieren (Caching!)
# Wenn du am Code was änderst, muss Docker Pandas nicht neu installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jetzt den Code kopieren
COPY . .

# Port freigeben
EXPOSE 6000

# Startbefehl für FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]