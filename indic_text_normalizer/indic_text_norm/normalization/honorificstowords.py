import regex as re
import json


def honorific2words(lang, text, dic):

    """
    Converts the honorifics (short forms) into words (full forms) using a language-specific dictionary.

    Args:
        text (str): The text which has to be normalized 
        lang_dict (dict): A dictionary that maps representation classes to their word equivalents in the specified language.

    Returns:
        str: Normalized text
    """


    honorific_regex = re.compile(create_regex_honourifics(dic['Honourific Titles']))
    hon_dict = dic['Honourific Titles']
    honorifics = honorific_regex.findall(text)
    for honorific in honorifics: 
            text = re.sub(honorific, f' {hon_dict[re.sub("[. ]","", honorific).strip()]} ', text)     
    return text

def create_regex_honourifics(dic):

    keys = dic.keys()
    p = ''
    for hon in keys:
        for char in ["{}".format(hon)]:
            finds = re.findall(r"\X", char, re.U) 

            if hon in ['RtHon','PhD']:
                x,y  = hon[:2],hon[2:].replace('.','')

                p += r'^{}?\s?.?{}.?\s?\s|\s{}.?\s?{}.?\s?\s|'.format(x,y,x,y)
                
            p += r'^{}.?\s|\s{}.?\s|'.format(''.join(finds), ''.join(finds))
    p = r'(?:{})'.format(p[:-1])
    return p

 