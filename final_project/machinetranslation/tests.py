import unittest
from translator import english_to_french, french_to_english
class TestEnglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hi'), 'Bonjour') # test when Hi is given as input the output is Bonjour.
        self.assertNotEqual(english_to_french('Hi'), 'Mesi') # test when Hi is given as input the output is not Mesi.

class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hi.
        self.assertNotEqual(french_to_english('Mesi'), 'Hello') # test when Mesi is given as input the output is not Hello.

unittest.main()