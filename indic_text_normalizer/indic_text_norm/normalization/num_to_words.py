from indic_numtowords import num2words
import regex as re
from functools import reduce




n2w = lambda nums, lang: {num: num2words(num, lang=lang) for num in nums}

def numtowords(lang,text):  

    """
    Converts a number into word using the indic_numtowords library
    Args:
        lang (str): The language code indicating the language of the text.
        text (str): Text that has to normalized.

    Returns:
        str: The text that has been normalized (numbers converted into their word representation).

    """

    num_regex = re.compile(r"(\s\d+\s)") #(?:(?<=\s)|^)(?=\s|$)
    numbers = num_regex.findall(text)
    try:
        n2w_dict = n2w(numbers, lang)
        for num in numbers:
            text = text.replace(num, f' {n2w_dict[num]} ')
    except Exception as e:
        #print(e)
        pass
    return text
           