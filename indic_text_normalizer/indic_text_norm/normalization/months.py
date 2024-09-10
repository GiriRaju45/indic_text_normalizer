import re

def months2words(lang, text, dic: dict):
    """
    Converts month names in a string into their word equivalents in the specified language.

    Args:
        lang (str): The language code indicating the language of the text.
        text (str): The input text containing month names.
        dic (dict): A dictionary that maps months to their word representations in the specified language.

    Returns:
        str: The input text with month names converted into words in the specified language.
    """
    months_dict = dic["Months"]
    months_regex = re.compile(r'\b(january|february|march|april|may|june|july|august|september|october|november|december)\b', re.IGNORECASE)

    result = ""
    last_pos = 0
    for match in months_regex.finditer(text):
        result += text[last_pos:match.start()]
        month = match.group(0).lower()
        result += months_dict.get(month, month)  # If no translation found, keep the original
        last_pos = match.end()
    
    result += text[last_pos:]
    return result
