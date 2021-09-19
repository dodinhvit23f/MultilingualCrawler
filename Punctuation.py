
def getPunctuationForLanguage(language):
    """
        :return Punctuation in dictionary follow language
        :key Vietnamese punctuation
        :var Language destination punctuaction
    """
    if(language == "km"):
        return {".": "\u17d4", "?": "\uff1f", "!": "\uff01", ";": ";", "...": "\u2026"}
    if(language == "zh"):
        return {".": "\u3002", "?": "?", "!": "!", ";": "；", "...": "..."}

    return {".": ".", "?": "?", "!": "!", ";": ";", "...": "..."}

