from fastapi import FastAPI
from app.models.sentiment_model import analyze_sentiment
import pandas as pd

DATA_PATH = "data/train.csv"

app = FastAPI()

@app.post("/add-training-data/")
def add_training_data(text: str, sentiment: str):
    # Validar entrada
    if sentiment not in ["positivo", "neutro", "negativo"]:
        raise HTTPException(status_code=400, detail="Sentimento inválido")

    # Adicionar dados ao arquivo
    new_data = pd.DataFrame({"text": [text], "sentiment": [sentiment]})
    new_data.to_csv(DATA_PATH, mode="a", header=False, index=False)

    return {"message": "Dados adicionados com sucesso!"}

@app.get("/")
def root():
    return {"message": "Bem-vindo à Biblioteca de Análise de Sentimento"}

@app.post("/analyze/")
def analyze_text(text: str):
    result = analyze_sentiment(text)
    return {"text": text, "analysis": result}
