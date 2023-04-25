import numpy as np
import string


class spellingBee:

    def __init__(self, number_letters=7, needed_letters=1, min_word_length=4):
        if number_letters < 0 or needed_letters < 0 or min_word_length < 0:
            print('Bad config')
            raise

        compulsory_letters, other_letters = self.get_allowed_letters(needed_letters, number_letters)
        all_words = np.loadtxt('word_files/scrabble_words.txt', dtype=str)
        all_words = self.filter_words_under_word_length(all_words, min_word_length)

        self.compulsory_letters = compulsory_letters
        self.other_letters = other_letters
        self.min_word_length = min_word_length
        self.all_words = all_words

    def get_allowed_letters(self, needed_letters, number_letters):
        letter_array = [letter for letter in string.ascii_uppercase]
        shuffled_letters = np.random.choice(letter_array, 7, replace=False)
        compulsory_letters = shuffled_letters[:needed_letters]
        other_letters = shuffled_letters[needed_letters:needed_letters + number_letters]
        return compulsory_letters, other_letters

    def filter_words_under_word_length(self, all_words, min_word_length):
        all_words = np.array([word for word in all_words if len(word) >= min_word_length])
        return all_words
