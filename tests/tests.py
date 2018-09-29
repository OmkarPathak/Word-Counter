from wordcounter import wordcounter
import unittest

class TestWordCount(unittest.TestCase):
    word_counter = wordcounter.WordCounter('The quick brown fox jumps over the lazy dog')

    def test_word_count(self):
        self.assertEqual(self.word_counter.get_word_count(), 9)

    def test_count_insensitive(self):
        self.assertEqual(self.word_counter.count('the'), 2)

    def test_count_sensitive(self):
        self.assertEqual(self.word_counter.count('the', ignore_case=False), 1)

    def test_word_frequencies(self):
        self.assertEqual(self.word_counter.get_word_frequencies(), {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})

if __name__ == '__main__':
    unittest.main()