import re

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    return text.strip()


if __name__ == "__main__":
    
    sample = "Breaking News!!! AI will replace all jobs."
    
    print(clean_text(sample))