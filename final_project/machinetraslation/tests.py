import unittest

from translator import english_to_french, french_to_english

class testTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Friendship'),'Amitié')
        self.assertEqual(english_to_french('Thank you'),'Merci')

    def test_frechToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Merci'),'Thank you')


if __name__=='__main__':
	unittest.main()