import pickle

# Carregar modelo e vetor
with open("models/sentiment_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
with open("models/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def analyze_sentiment(text: str):
    # Transformar texto em vetor
    text_vector = vectorizer.transform([text])

    # Fazer a previsão
    prediction = model.predict(text_vector)
    confidence = max(model.predict_proba(text_vector)[0])  # Probabilidade da previsão

    return {"sentiment": prediction[0], "confidence": confidence}
