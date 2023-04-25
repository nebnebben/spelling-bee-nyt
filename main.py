from brute_force import BruteForce
from spelling_bee import spellingBee
import timeit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spelling_bee = spellingBee(min_word_length=4)
    brute_force = BruteForce(spelling_bee.all_words, spelling_bee.compulsory_letters, spelling_bee.other_letters)
    print(spelling_bee.compulsory_letters)
    print(spelling_bee.other_letters)
    result = brute_force.solve()
    print(result[:10])
    # print(timeit.timeit(lambda: brute_force.solve(), number=20))
