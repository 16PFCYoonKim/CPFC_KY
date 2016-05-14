def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split('')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_words(words):
    """prints the word after popping it off"""
    word = words.pop(0)
    print word

def print_las_word(wors):
    """Print the last wor after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the second words"""
    words = break_words(sentence)
    return sort_words(words)

