
class BruteForce:

    def __init__(self, all_words, compulsory_letters, other_letters):

        self.all_words = all_words
        self.compulsory_letters = compulsory_letters
        self.other_letters = other_letters

    def solve(self):
        final_list = []
        for word in self.all_words:
            if self.check_word(word):
                final_list.append(word)
        return final_list

    def check_word(self, word):
        used_compulsory_letters = all([True if letter in word else False for letter in self.compulsory_letters])
        only_used_allowed_letters = all([True if letter in self.other_letters or letter in self.compulsory_letters else False for letter in word])
        return used_compulsory_letters and only_used_allowed_letters
