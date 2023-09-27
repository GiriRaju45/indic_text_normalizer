import regex as re
from functools import reduce
import json






def cardinals2words(lang, text, dic: dict):
    
    """
    Converts a cardinal number into words using a language-specific dictionary.
    The current limit of the no.of cardinals is set to 31st

    Args:
        lang (str): The language code indicating the language of the text.
        number (str): The cardinal number to be converted (e.g., "22nd or 22 nd").
        lang_dict (dict): A dictionary that maps cardinal numbers to their word representations in the specified language.

    Returns:
        str: The input cardinal number converted into words.

    """  

    regex_cardinals = {
        "as": r"(?:^|\s.?)(?:[১-৯]|[১২][০-৯]|৩[০১])[\s?তম|\s?ম|\s?র্থ|\s?য়|\s?ম]+\b",
        "brx": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])\s?था\b",
        "bn": r"(?:^|\s.?)(?:[১-৯]|[১২][০-৯]|৩[০১])[\s?তম|\s?ম|\s?র্থ|\s?য়|\s?ম|\s?ষ্ঠ]+\b",
        "dgr": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?ला|\s?आ|\s?था|\s?मां]+\b",
        "en": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?rd|\s?st|th|nd]+\b",
        "gu": r"(?:^|\s.?)(?:[૧-૯]|[૧૨][૦-૯]|૩[૦૧])[\s?મું|\s?ઠ્ઠું|\s?થું|\s?જું|\s?લું]+\b",
        "hi": r"(?:^|\s.?)(?:[१-९]|[१२][०-९]|३[०१])[\s?ला|\s?रा|\s?था|\s?वाँ]+\b",
        "kn": r"(?:^|\s.?)(?:[೧-೯]|[೧೨][೦-೯]|೨[೦೧])[\s?ನೇ]+\b",
        "knk": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?लें|\s?रें|\s?थें|\s?वें]+\b",
        "ks": r"\s*(?:[۱-۹]|[۱۲][٠-۹]|۳[٠۱])(?:ہِم|یِم|ژِم|رِم|ٹِھم)\b",
        "ml": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[)൦]+\b",
        "mn": r"(?:[꯱-꯹]|[꯱꯲][꯰-꯹]|꯳[0꯱])[\s?ꯁꯨꯕꯥ|\s?ꯇꯥ|\s?ꯗꯥ]+\b",
        "mr": r"(?:[1-9]|[12][0-9]|3[01])[\s?वा|\s?रा|\s?था|\s?वी]+\b",
        "np": r"(?:^|\s.?)(?:[१-९]|[१२][०-९]|३[०१])[\s?औँ|\s?औं]+\b",
        "sa": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?rd|\s?st|th|nd]+\b",
        "or": r"(?:^|\s.?)(?:[୧-୯]|[୧୨][୦-୯]|୩[୦୧])[\s?ମ|\s?ଶ|\s?ଷ୍ଠ|\s?ର୍ଥ|\s?ୟ]+\b",
        "sat": r"(?:^|\s.?)(?:[᱑-᱙]|[᱑᱒][᱐-᱙]|᱓[᱐᱑])[\s?ᱟᱱ|\s?ᱟᱨ|\s?ᱞᱳ]+\b",
        "sin": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?rd|\s?st|th|nd]+\b",
        "te": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])\s?వ\b",
        "ta": r"(?:^|\s.?)(?:[1-9]|[12][0-9]|3[01])[\s?ஆம்|\s?வது]+\b",
        "ur": r"\s*(?:[۱-۹]|[۱۲][٠-۹]|۳[٠۱])(?:\s?واں)"
    }

    cardinals_dict = dic["Cardinals"]
    cardinal_regex = re.compile(regex_cardinals[lang])
    
    cardinal_finds = cardinal_regex.findall(text)
    
    for cardinal in cardinal_finds:
        normalized_cardinal = cardinals_dict.get(re.sub(r"[\. ]", "", cardinal).strip())
        if normalized_cardinal is not None:
            text = text.replace(cardinal, f" {normalized_cardinal} ")

    return text

