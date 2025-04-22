from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# Tworzymy aplikację FastAPI
app = FastAPI()

# Odczytanie zmiennej środowiskowej (np. klucz API)
API_KEY = os.getenv("API_KEY", "brak_klucza")

# Inicjalizacja i trenowanie modelu
model = LinearRegression()
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 6, 8, 10])
model.fit(X_train, y_train)

# Klasa do walidacji danych wejściowych
class InputData(BaseModel):
    values: Optional[List[float]] = None

# Endpoint główny
@app.get("/")
def home():
    return {"message": "Witaj w API!"}

# Endpoint do predykcji
@app.post("/predict")
def predict(data: InputData):
    if data.values is None:
        raise HTTPException(status_code=400, detail="Brak danych wejściowych")

    X_input = np.array(data.values).reshape(-1, 1)
    prediction = model.predict(X_input).tolist()
    return {"prediction": prediction}

# Endpoint z informacjami o modelu
@app.get("/info")
def info():
    return {"model": "Linear Regression", "features": 1}

# Endpoint do sprawdzania zdrowia serwera
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint pokazujący wartość zmiennej środowiskowej
@app.get("/api-key")
def get_api_key():
    return {"api_key": API_KEY}

# Uruchamianie serwera (dla lokalnego uruchomienia)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
