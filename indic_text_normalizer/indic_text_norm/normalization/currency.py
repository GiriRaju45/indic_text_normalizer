import regex as re
from functools import reduce


def currencies2words(lang, text, dic):
    
    """
    Converts a currency amount into words using a language-specific dictionary.

    Args:
        lang (str): The language code indicating the language of the text.
        amount (str): The currency amount to be converted (e.g. "$100").
        lang_dict (dict): A dictionary that maps currency codes to their word representations in the specified language.

    Returns:
        str: The input currency amount converted into words.
        (Ex:  'En' : "$100 -> 100 Dollars ").
    """

    currencies_dict = dic["Currency"]

    reg = "|".join(
        f"\{curr}\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?" for curr in currencies_dict

    )
    # print(reg)
    currency_regex = [
        r"\s\₹\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\$\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\€\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\£\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\¥\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\₣\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|]",
        r"\s\﷼\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\원\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\¥\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\฿\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\s\₽\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})? ?د.ك.\s|",
        r"[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?د.إ\s",
        r"|\skr\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\₺\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?|",
        r"\szł\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?"
    ]
    currency_regex = "".join(reg for reg in currency_regex)
    currency_regex = re.compile(r"(?:{})+".format(currency_regex))
    finds = currency_regex.findall(text)
    for find in finds:
        text = text.replace(
            find,
            f' {find.replace(re.sub(r"[, 0-9]", "", find),"")} '
            + currencies_dict
    [re.sub(r"[, 0-9]", "", find)],
        )

    return text
