import regex as re
import json
from functools import reduce

# A language specific dictionary for regex creation
# dvn key includes all the languages that use the Devangari script as common 

lang_dict = json.load(open('/home/ai4bharat/indic_text_normalizer/indic_text_norm/data/ta.json', encoding= 'utf-8'))


bi_syl_regex = {} 

bi_syl_regex['dvn'] = r'\s[०-९]+/?\.?[०-९]*\s?\.?{}\.?\s?{}\.?\s|^[०-९]+/?\.?[०-९]*\s\.?{}\s?\.?{}\.?\s|\s[०-९]+/?\.?[०-९]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['tel'] = r'\s[౦-౯]+/?\.?[౦-౯]*?\s?\.?{}\.?\s?{}\.?\s|^[౦-౯]+/?\.?[౦-౯]*\s\.?{}\s?\.?{}\.?\s|\s[౦-౯]+/?\.?[౦-౯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['kan'] = r'\s[೦-೯]+/?\.?[೦-೯]*?\s?\.?{}\.?\s?{}\.?\s|^[೦-೯]+/?\.?[೦-೯]*\s\.?{}\s?\.?{}\.?\s|\s[೦-೯]+/?\.?[೦-೯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['guj'] = r'\s[૦-૯]+/?\.?[૦-૯]*?\s?\.?{}\.?\s?{}\.?\s|^[૦-૯]+/?\.?[૦-૯]*\s\.?{}\s?\.?{}\.?\s|\s[૦-૯]+/?\.?[૦-૯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['mni'] = r'\s[꯰-꯹]+/?\.?[꯰-꯹]*?\s?\.?{}\.?\s?{}\.?\s|^[꯰-꯹]+/?\.?[꯰-꯹]*\s\.?{}\s?\.?{}\.?\s|\s[꯰-꯹]+/?\.?[꯰-꯹]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['ori'] = r'\s[୦-୯]+/?\.?[୦-୯]*?\s?\.?{}\.?\s?{}\.?\s|^[୦-୯]+/?\.?[୦-୯]*\s\.?{}\s?\.?{}\.?\s|\s[୦-୯]+/?\.?[୦-୯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['urd'] = r'[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})|^[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})|[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})$|[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})|^[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})|[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})$|'
bi_syl_regex['kas'] = r'[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})|^[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})|[۰-۹]+/?\.?[۰-۹]*?\s*(?:{}\s*?{}|{}\s*?{})$|[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})|^[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})|[0-9]+/?\.?[0-9]*?\s*(?:{}\s*?{}|{}\s*?{})$|'
bi_syl_regex['asm'] = r'\s[০-৯]+/?\.?[০-৯]*?\s?\.?{}\.?\s?{}\.?\s|^[০-৯]+/?\.?[০-৯]*\s\.?{}\s?\.?{}\.?\s|\s[০-৯]+/?\.?[০-৯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['ben'] = r'\s[০-৯]+/?\.?[০-৯]*?\s?\.?{}\.?\s?{}\.?\s|^[০-৯]+/?\.?[০-৯]*\s\.?{}\s?\.?{}\.?\s|\s[০-৯]+/?\.?[০-৯]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['sat'] = r'\s[᱐-᱙]+/?\.?[᱐-᱙]*?\s?\.?{}\.?\s?{}\.?\s|^[᱐-᱙]+/?\.?[᱐-᱙]*\s\.?{}\s?\.?{}\.?\s|\s[᱐-᱙]+/?\.?[᱐-᱙]*\s?\.?{}\s?\.?{}\.?$|\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['eng'] = r'\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'
bi_syl_regex['tam'] = r'\s[0-9]+/?\.?[0-9]*?\s?\.?{}\.?\s?{}\.?\s|^[0-9]+/?\.?[0-9]*\s\.?{}\s?\.?{}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{}\s?\.?{}\.?$|'

dvn = ['brx', 'doi', 'hin', 'mar', 'kok', 'nep', 'san', 'snd'] #mai


def metrics2words(lang: str, text: str, lang_dict: dict):                                       
    
    """
    Converts short-form metrics in a given text into their full form using a language-specific dictionary.

    Args:
        lang (str): The language code indicating the language of the text.
        text (str): The input text containing short-form metrics to be converted.
        lang_dict (dict): A dictionary that maps short-form metrics to their full form in the specified language.

    Returns:
        str: The input text with short-form metrics replaced by their full-form equivalents.
    """

    met_dict = lang_dict["Metrics and SI Units"]
    re_pattern = re.compile(create_all_regex_metrics(lang, met_dict))

    metrics = re_pattern.findall(text)
    

    new_dict = {f_norm: re.sub(re.sub('[0-9]?.?/?[0-9]','',f_norm),f' {met_dict[re.sub("[0-9./ ]", "", f_norm).strip()]} ', f_norm) for f_norm in metrics}


    text = reduce(lambda x,y: x.replace(*y), [text, *list(new_dict.items())])

    return text


def create_all_regex_metrics(lang, dic: dict):
    key_metrics = list(dic.keys())

    # exception of two character short forms metrices
    bi_char_exp = [ "टन", "घंटा", "ha", "hr", "ટન", "ગ્રા", "கிலோ", "மணி", "நொடி", "টন", "ಗ್ರಾಂ", "ಚಮೀ", "గ్రా", "చమీ", "ఎఫ్", "ٹن", "سۍ", "جی", "ଟନ୍‌"] 

    # kashmiri/urdu single character metrices
    ks_single = ["ٹن", "سۍ", "جی"]

    # exception of three character short form metrices
    tri_char_exp = ["मिनट", "सेकंड", "ग्राम", "ঘন্টা", "মিনিট", "ಚಸೆಂಮೀ", "ಚಕಿಮೀ", "చసెంమీ", "చకిమీ", "ചസെമീ", "min", "sec", "sqm", "ବସେମି", "ବକିମି", "ᱯᱷᱹ"]
    
    # list of prefix - sq in short forms in all languages
    sq_word_all_lang = [ "वर्ग", "sq", "સ્ક્વે", "சதுர", "বর্গ", "ಚ", "ᱵᱚᱨ", "చ", "مربع",  "ച", "ବ", "ꯁ꯭ꯛꯕ꯭ꯌꯥ", "ꯑꯦꯜ", "चौसें"]

    def find_sq(word):

        # This function helps to find the prefix that is equivalent to sq in a given words
        
        for partition in sq_word_all_lang:
            if partition in word:
                return partition

    r = r""
    for key in key_metrics:
        
        for char in ["{}".format(key)]:

            finds = re.findall(r"\X", char, re.U) 
            
            # fst_syl -> First part syllable/character of the metrics
            # scnd_syl -> second part syllable/character of the metrics

            # Santhali language since the 2 char short form is equal to 4 char
            if lang == "sat" and len(finds) == 4:
                fst_syl, scnd_syl = finds[:2], finds[:2]
                pattern += bi_syl_regex['sat'].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)#f"\s[0-9]+/?\.?[0-9]*\s?\.?{x}\.?{y}\.?\s|^[0-9]*\.?[0-9]*\s?\.?{x}\.?{y}\.?\s|\s[0-9]*\.?[0-9]*\s?\.?{x}\.?{y}\.?$|"
                r += pattern
            
            # Kashmiri/Urdu language regex creation for metrices with 2 characters
            elif (lang == 'kas' or lang == 'urd') and len(finds) == 2 and key not in bi_char_exp:
                fst_syl, scnd_syl = key[0], key[1]
                pattern = bi_syl_regex['urd'].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)
                r += pattern

            # Kashmiri/Urdu language regex creation for the square equivalent
            elif (lang == 'kas' or lang == 'urd') and find_sq(key) is not None:
                matched_partition = find_sq(key)
                fst_syl, scnd_syl = key[: len(matched_partition)], key[len(matched_partition) :]
                
                pattern = f"[0-9]+/?\.?[0-9]*?\s{fst_syl}\s*{scnd_syl}\s|[0-9]+/?\.?[0-9]*?\s{fst_syl}\s*{scnd_syl}\s$|^[0-9]+/?\.?[0-9]*?\s{fst_syl}\s*{scnd_syl}\s"
                r += f"{pattern}|"

            elif (lang == 'kas' or lang == 'urd') and key in ks_single:
                pattern = f"\d*\.\d+?\s*{key}\s"
                r += f"{pattern}|"

            # two char representation regex creation
            elif len(finds) == 2 and key not in bi_char_exp: # finds the 2char metrics except the short forms in bi_char_exp
                
                # Devanagari script using languages
                if lang in dvn:
                    fst_syl, scnd_syl = finds[0], finds[1]
                    pattern = bi_syl_regex['dvn'].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)
                    r += pattern  

                # Languages other than Devanagari scripted. 
                else:
                    fst_syl, scnd_syl = finds[0], finds[1]
                    pattern = bi_syl_regex[lang].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)


            # regex creation for the words contain the prefix sq in all languages
            elif find_sq(key) is not None :
                matched_partition = find_sq(key)
                
                # Devanagari
                if matched_partition is not None and lang in dvn:
                    fst_syl, scnd_syl = key[: len(matched_partition)], key[len(matched_partition) :]
                    r += bi_syl_regex['dvn'].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)
                
                elif matched_partition is not None:
                    fst_syl, scnd_syl = key[: len(matched_partition)], key[len(matched_partition) :]
                    r += bi_syl_regex[lang].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)

            # regex creation for the two char metrics that is represented as three. Ex: ग्राम 
            elif len(finds) == 3 and key not in tri_char_exp and lang not in ['ks', 'ur']:
                if lang in dvn:
                    fst_syl, scnd_syl = finds[0], "".join(finds[1:])
                    r += bi_syl_regex['dvn'].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)
                else:
                    fst_syl, scnd_syl = finds[0], "".join(finds[1:])
                    r += bi_syl_regex[lang].format(fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl,fst_syl, scnd_syl)
            # regex creation for the metrics that are not in the all above cases
            else:
    
                r += f"\s[0-9]+/?\.?[0-9]*\s?\.?{key}\.?\s|^[0-9]+/?\.?[0-9]*s?\.?{key}\.?\s|\s[0-9]+/?\.?[0-9]*\s?\.?{key}\.?$|"
        
    
           
    r = r[:-1]
    return r"[{}]+".format(r)
