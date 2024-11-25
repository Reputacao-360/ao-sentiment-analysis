import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle
 
DATA_PATH = "data/train.csv"

def train_sentiment_model():
    # Carregar dados
    data = pd.read_csv(DATA_PATH)
    texts = data["text"]
    labels = data["sentiment"]

    # Dividir em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # Vetorização do texto (transformar texto em vetores numéricos)
    vectorizer = CountVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)

    # Treinar modelo
    model = MultinomialNB()
    model.fit(X_train_vectors, y_train)

    # Avaliar modelo
    predictions = model.predict(X_test_vectors)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Precisão do modelo: {accuracy * 100:.2f}%")

    # Salvar modelo e vetor
    with open("models/sentiment_model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    with open("models/vectorizer.pkl", "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

if __name__ == "__main__":
    train_sentiment_model()
