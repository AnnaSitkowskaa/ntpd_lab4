# ntpd_lab4
Instrukcje uruchamiania aplikacji
1. Lokalnie
Zainstaluj zależności:
pip install -r requirements.txt

Uruchom aplikację:
uvicorn app:app --reload
Aplikacja będzie dostępna pod http://localhost:8000.

2. Za pomocą Dockera
Zbuduj obraz:
docker build -t ntpd_lab4 .
Uruchom kontener:
docker run -p 5000:5000 ntpd_lab4
Aplikacja będzie dostępna pod http://localhost:5000.

3. Za pomocą Docker Compose
Uruchom aplikację i inne usługi:
docker-compose up
Aplikacja będzie dostępna pod http://localhost:5000.

Parametry konfiguracyjne
Zmienne środowiskowe (np. w .env):

APP_PORT=5000

DEBUG=True

Zasoby:

Pamięć: 1 GB RAM

CPU: Możliwość konfiguracji w docker-compose.yml.

GitHub - ntpd_lab4
