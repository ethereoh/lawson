from keybert import KeyBERT

kw_model = KeyBERT()

def get_keywords(payload): 
    keywords = kw_model.extract_keywords(payload)
    return keywords