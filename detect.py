from preprocess import clean_text

fake_keywords = [
    "shocking",
    "breaking",
    "secret",
    "click here",
    "viral"
]

def detect_fake_news(text):
    
    text = clean_text(text)
    
    score = 0
    
    for keyword in fake_keywords:
        if keyword in text:
            score += 1
    
    if score >= 2:
        return "Fake News"
    
    return "Real News"


if __name__ == "__main__":
    
    news = "Breaking shocking secret revealed"
    
    print(detect_fake_news(news))