import re
from indic_numtowords import num2words

def number(s, lang):
    """
    Transforms all numeric sequences found within a string by converting them into words in Hindi.

    Args:
        s (str): The input string that contains numeric sequences.
        lang (str): The language code for converting numeric characters into words.

    Returns:
        str: The input string with numeric sequences transformed, where numbers are replaced 
             with their word equivalents in Hindi.
    """
    output = s  
    phone_num_regex = re.compile(r'\b\d+\b') 
    matches = phone_num_regex.findall(s)
    if matches:
        for number in matches:
            transformed_number = num2words(number, lang=lang, variations=False)
            output = output.replace(number, transformed_number)
            output = re.sub(r'\s+', ' ', output.strip())
    return output