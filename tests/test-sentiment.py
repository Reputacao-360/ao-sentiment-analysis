from app.models.sentiment_model import analyze_sentiment

def test_positive_sentiment():
    result = analyze_sentiment("O serviço foi excelente!")
    assert result["sentiment"] == "positivo"

def test_negative_sentiment():
    result = analyze_sentiment("O atendimento foi horrível.")
    assert result["sentiment"] == "negativo"

def test_neutral_sentiment():
    result = analyze_sentiment("O produto está disponível.")
    assert result["sentiment"] == "neutro"
