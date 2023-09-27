import regex as re
from functools import reduce


def fractions2words(lang, text, lang_dic):
    
    """
    Converts a fractional number into words using a language-specific dictionary.

    Args:
        lang (str): The language code indicating the language of the text.
        fraction (str): The fractional number to be converted (e.g., "1/4").
        lang_dict (dict): A dictionary that maps fractional representations to their word equivalents in the specified language.

    Returns:
        str: The input fractional number converted into words.

    """

    fraction_dict = lang_dic["Fractions"]
    fractions_regex = "|".join(fraction for fraction in fraction_dict)
    fractions_regex = re.compile(r"\b(?:{})\b+".format(fractions_regex))
    finds = fractions_regex.findall(text)
    find_dict = {find: fraction_dict[find] for find in finds}

    text = reduce(lambda x, y: x.replace(*y), [text, *list(find_dict.items())])
    return text
