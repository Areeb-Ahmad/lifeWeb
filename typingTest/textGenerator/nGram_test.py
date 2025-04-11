import unittest
from textGenerator_nGram import NGramTextGenerator


class TestNGramTextGenerator(unittest.TestCase):
    def setUp(self):
        self.corpus = (
            "The quick brown fox jumps over the lazy dog. "
            "The slow green turtle crawls under the sleepy cat."
        )
        self.generator = NGramTextGenerator(n=3)
        self.generator.build_model(self.corpus)

    def test_generate_length(self):
        output = self.generator.generate(length=10)
        words = output.split()
        self.assertGreaterEqual(len(words), 8)  # allow for early termination
        self.assertLessEqual(len(words), 10)

    def test_model_is_not_empty(self):
        self.assertGreater(len(self.generator.model), 0)

    def test_starts_are_populated(self):
        self.assertGreater(len(self.generator.starts), 0)

    def test_serialization(self):
        self.generator.save_model("test_model.pkl")
        new_gen = NGramTextGenerator()
        new_gen.load_model("test_model.pkl")
        self.assertEqual(new_gen.n, self.generator.n)
        self.assertEqual(new_gen.model, self.generator.model)
        self.assertEqual(new_gen.starts, self.generator.starts)


if __name__ == '__main__':
    unittest.main()
