import regex as re
import json
import os

from cardinals import cardinals2words
from currency import currencies2words
from fraction import fractions2words
from metrics import metrics2words
from num_to_words import numtowords
from honorificstowords import honorific2words
from phone_number import phone2words
from pan_card import pancard2words
from adhaar_card import adhaarcard2words
from months import months2words

parent_file_path = '../data'
lang2jsons = os.listdir(parent_file_path)

class Normalizer():

    def __init__(self):


        self.lang_jsons = {}
        for json_ in lang2jsons:
            self.lang_jsons[json_.split('.')[0]] = json.load(open(os.path.join(parent_file_path, json_), encoding= 'utf-8'))
     

    def normalizer(self, text: str, lang):
        
        """
        Performs the normalization on the given text and returns the normalized text.

        Args:
        text (str): The text that has to be normalized.
        lang (str): The language code of the given input text.

        Returns:
        text (str): The normalized text.

        """

        text = phone2words(lang, text)
        text = adhaarcard2words(lang, text)
        text = pancard2words(lang, text)
        text = months2words(lang, text, self.lang_jsons[lang])
        text = currencies2words(lang, text, self.lang_jsons[lang])
        text = cardinals2words(lang, text, self.lang_jsons[lang])
        text = metrics2words(lang, text, self.lang_jsons[lang])
        text = fractions2words(lang, text, self.lang_jsons[lang])
        text = honorific2words(lang, text, self.lang_jsons[lang])
        text = numtowords(lang, text)
       
        return text


hi = "My birthday comes in September!!"

norm = Normalizer()

print(norm.normalizer(hi, 'hin'))