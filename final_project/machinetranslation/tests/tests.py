"""
Test Class for translator.py methods by Gabriele Cano
"""
import unittest
import os
from dotenv import load_dotenv
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Test cases for english_to_french method
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        text_to_translate = 'Hello'
        result = english_to_french(text_to_translate)
        self.assertEqual(result, "Bonjour")
    def test_empty_string(self):
        """
        Test an empty string
        """
        text_to_translate = ''
        result = english_to_french(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_null_string(self):
        """
        Test a null string
        """
        text_to_translate = None
        result = english_to_french(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_numeric_value(self):
        """
        Test a numeric value
        """
        text_to_translate = 458
        result = english_to_french(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_non_existent_word(self):
        """
        Test a null string
        """
        text_to_translate = "sjkahdajsd"
        result = english_to_french(text_to_translate)
        self.assertEqual(result, 'Sorry, I can\'t find a translation for the text: '
        + text_to_translate)


class TestFrenchToEnglish(unittest.TestCase):
    """
    Test cases for french_to_english method
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        text_to_translate = 'Bonjour'
        result = french_to_english(text_to_translate)
        self.assertEqual(result, "Hello")
    def test_empty_string(self):
        """
        Test an empty string
        """
        text_to_translate = ''
        result = french_to_english(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_null_string(self):
        """
        Test a null string
        """
        text_to_translate = None
        result = french_to_english(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_numeric_value(self):
        """
        Test a numeric value
        """
        text_to_translate = 9875
        result = french_to_english(text_to_translate)
        self.assertEqual(result, "You have entered an empty text or a number. Please retry.")
    def test_non_existent_word(self):
        """
        Test a null string
        """
        text_to_translate = "pldslaodlsao"
        result = french_to_english(text_to_translate)
        self.assertEqual(result, 'Sorry, I can\'t find a translation for the text: '
        + text_to_translate)


class TestAssertEnvironmentVariables(unittest.TestCase):
    """
    Test cases for environments variables
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']
        self.assertTrue(len(apikey) > 0)
        self.assertTrue(len(url) > 0)

unittest.main()
