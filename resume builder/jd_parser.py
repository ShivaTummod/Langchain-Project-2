# jd_parser.py
import re

def extract_keywords(text):
    keywords = re.findall(r'\b(Java|Python|Django|AI|ML|LLM|REST|SQL|NLP|Teamwork|Leadership)\b', text, re.I)
    return list(set([kw.lower() for kw in keywords]))
