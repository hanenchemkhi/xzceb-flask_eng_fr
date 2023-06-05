"""
Module translates a text from english to french and from french to english
 using IBM MyMemoryTrnaslator translator
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates a text from English to French using IBM MyMemoryTranslator.
    
    Args:
        english_text (str): The text to be translated.
    
    Returns:
        str: The translated text in French.
    """
    translator = MyMemoryTranslator(source='en',target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates a text from French to English using IBM MyMemoryTranslator.
    
    Args:
        french_text (str): The text to be translated.
    
    Returns:
        str: The translated text in English.
    """
    return MyMemoryTranslator(source='fr', target='en').translate(french_text)
