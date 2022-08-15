"""
def check_anagram():

    This function should determine if two words are anagrams. An anagram is a word or phrase
    that can be formed by rearanging the letters of another word or phrase.

    :param first: The first word.
    :param second: The second word.
    :return: True if the words are anagrams, otherwise False.

    >>> check_anagram('listen', 'silent')
    True

    >>> check_anagram('horses', 'houses')
    False
    """

def check_anagram(a, b):
    for ch in a:
        if ch in b:
            a = a[1:]
    if a:
        print("False")
    else:
        print("True")


check_anagram('listen', 'silent')
check_anagram('horses', 'houses')
