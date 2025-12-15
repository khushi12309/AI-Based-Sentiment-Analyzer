def analyze_sentiment(text):
    text = text.lower()

    positive_words = ["good", "great", "happy", "excellent", "love", "amazing"]
    negative_words = ["bad", "sad", "worst", "hate", "poor", "angry"]

    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    else:
        return "Neutral"
