def detect_language(text):
    return "ar" if any("\u0600" <= c <= "\u06FF" for c in text) else "en"
