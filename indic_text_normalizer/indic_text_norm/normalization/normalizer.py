import regex as re
import json
import os

from cardinals import cardinals2words
from currency import currencies2words
from fraction import fractions2words
from metrics import metrics2words
from num_to_words import numtowords
from honorificstowords import honorific2words

parent_file_path = 'data'
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
   
        text = currencies2words(lang, text, self.lang_jsons[lang])
        text = cardinals2words(lang, text, self.lang_jsons[lang])
        text = metrics2words(lang, text, self.lang_jsons[lang])
        text = fractions2words(lang, text, self.lang_jsons[lang])
        text = honorific2words(lang, text, self.lang_jsons[lang])
        text = numtowords(lang, text)

       
        return text


ta = "வணக்கம் Dr. ராகுல். என் மகனின் 1 வது பிறந்த நாள். என்னிடம் $4000 உள்ளது. நான் வரிசையில் நின்று 1/2 லி மாம்பழச்சாறு வாங்கினேன். என்னிடம் 1500சதுர.மீ இடம் உள்ளது, இன்றைக்கு தேதி 21 இல்லை 20 ஆ?"

norm = Normalizer()

print(norm.normalizer(ta, 'ta'))