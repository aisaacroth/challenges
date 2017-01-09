from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary_file:
        return [line.strip() for line in dictionary_file]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(word_list or load_words(), key=calc_word_value)


if __name__ == "__main__":
    pass  # run unittests to validate
