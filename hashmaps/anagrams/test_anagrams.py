import unittest

class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        from anagrams import is_anagram
        self.is_anagram = is_anagram

    def test_basic_anagram(self):
        self.assertTrue(self.is_anagram("listen", "silent"))

    def test_not_anagram(self):
        self.assertFalse(self.is_anagram("hello", "world"))

    def test_different_lengths(self):
        self.assertFalse(self.is_anagram("abc", "ab"))

    def test_same_string(self):
        self.assertTrue(self.is_anagram("python", "python"))

    def test_empty_strings(self):
        self.assertTrue(self.is_anagram("", ""))

    def test_case_sensitive(self):
        self.assertFalse(self.is_anagram("Listen", "silent"))

    def test_with_spaces(self):
        self.assertFalse(self.is_anagram("a gentleman", "elegant man"))  # not strict anagram unless spaces are removed

    def test_with_special_characters(self):
        self.assertTrue(self.is_anagram("123!@#", "@#321!"))

    def test_unicode_characters(self):
        self.assertTrue(self.is_anagram("åäö", "öåä"))

if __name__ == '__main__':
    unittest.main()