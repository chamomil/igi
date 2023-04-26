import unittest
from sentence_parsing import sentences, average_length, ngrams


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sentences("Hello! How are you?"), (2, 2))

    def test2(self):
        self.assertEqual(sentences("dfksb"), (0, 0))

    def test3(self):
        self.assertEqual(sentences("Hi. Mr. Hampton, how are you?"), (2, 1))

    def test4(self):
        self.assertEqual(average_length("Hello! How are you?", 2)[1], 7)
        self.assertEqual(average_length("Hello! How are you?", 2)[2], 3.5)

    def test5(self):
        self.assertEqual(average_length("Hello! How a287re 34567?", 2)[1], 7)
        self.assertAlmostEqual(average_length("Hello! How a287re 34567?", 2)[2], 4.6667, delta=0.001)

    def test6(self):
        self.assertEqual(ngrams(['Hello', 'How', 'are', 'you'], 4), {'Hello How are you ': 1})

if __name__ == '__main__':
    unittest.main()