import re

def symbols2words(text, dic):
    """
    Converts symbols in a string into their word equivalents based on the provided dictionary.
    Adds a single space before and after the symbol, unless specific punctuation marks follow the symbol.

    Args:
        text (str): The input text containing symbols.
        dic (dict): A dictionary that maps symbols to their word representations.

    Returns:
        str: The input text with symbols converted into words.
    """
    symbols_dict = dic["Symbols"]

    for symbol, word in symbols_dict.items():
        text = re.sub(f'{re.escape(symbol)}(?=\s*[,.!?])', f' {word[0]}', text)
        text = text.replace(symbol, f' {word[0]} ')

    text = re.sub(r'^\s+|\s+', ' ', text).strip()
    
    return text



