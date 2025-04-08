# ntpd_lab4
Instrukcje uruchamiania aplikacji
1. Lokalnie
Zainstaluj zależności:

bash
Kopiuj
Edytuj
pip install -r requirements.txt
Uruchom aplikację:

bash
Kopiuj
Edytuj
uvicorn app:app --reload
Aplikacja będzie dostępna pod http://localhost:8000.

2. Za pomocą Dockera
Zbuduj obraz:

bash
Kopiuj
Edytuj
docker build -t ntpd_lab4 .
Uruchom kontener:

bash
Kopiuj
Edytuj
docker run -p 5000:5000 ntpd_lab4
Aplikacja będzie dostępna pod http://localhost:5000.

3. Za pomocą Docker Compose
Uruchom aplikację i inne usługi:

bash
Kopiuj
Edytuj
docker-compose up
Aplikacja będzie dostępna pod http://localhost:5000.

Parametry konfiguracyjne
Zmienne środowiskowe (np. w .env):

APP_PORT=5000

DEBUG=True

Zasoby:

Pamięć: 1 GB RAM

CPU: Możliwość konfiguracji w docker-compose.yml.

Repozytorium GitHub
GitHub - ntpd_lab4
