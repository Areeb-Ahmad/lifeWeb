import random
import pickle
from collections import defaultdict
from typing import List, Tuple
import string


class NGramTextGenerator:
    def __init__(self, n: int = 3):
        if n < 2:
            raise ValueError("n must be at least 2")
        self.n = n
        self.model = defaultdict(list)
        self.starts = []

    def build_model(self, text: str):
        # Convert text to lowercase before building the model
        text = text.lower()
        words = text.split()
        if len(words) < self.n:
            raise ValueError("Text is too short to build the model")

        self.model.clear()
        self.starts.clear()

        for i in range(len(words) - self.n + 1):
            prefix = tuple(words[i:i + self.n - 1])
            next_word = words[i + self.n - 1]
            self.model[prefix].append(next_word)
            if i == 0 or words[i - 1].endswith(('.', '!', '?')):  # possible new sentence
                self.starts.append(prefix)

    def generate(self, length: int = 50, strip_punctuation: bool = True) -> str:
        if not self.model:
            return ""

        prefix = random.choice(self.starts)
        result = list(prefix)

        for _ in range(length - self.n + 1):
            next_words = self.model.get(prefix)
            if not next_words:
                break
            next_word = random.choice(next_words)
            result.append(next_word)
            prefix = tuple(result[-(self.n - 1):])

        output = ' '.join(result)

        if strip_punctuation:
            additional_punctuation = "‘’“”…—"
            all_punctuation = string.punctuation + additional_punctuation
            output = output.translate(str.maketrans('', '', all_punctuation))
        return output

    def save_model(self, filepath: str):
        with open(filepath, 'wb') as f:
            pickle.dump((self.n, self.model, self.starts), f)

    def load_model(self, filepath: str):
        with open(filepath, 'rb') as f:
            self.n, self.model, self.starts = pickle.load(f)
