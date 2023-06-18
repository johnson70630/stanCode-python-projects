"""
File: anagram.py
Name: Johnson
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    The program prints all anagrams.
    """

    ####################
    while True:
        print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
        s = input("Find anagrams for: ")
        start = time.time()
        if s == EXIT:
            break
        all_anagrams = find_anagrams(s)
        print(f"{len(all_anagrams)} anagrams:{all_anagrams}")
    end = time.time()
    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    with open(FILE, 'r') as f:
        dictionary = set()
        for line in f:
            vocabularies = line.split()
            for vocab in vocabularies:
                if len(vocab) == len(s):
                    dictionary.add(vocab)
    return dictionary


def find_anagrams(s):
    """
    :param s: str
    :return: anagrams: lst
    """
    print('Searching...')
    dic = read_dictionary(s)
    all_anagram = []
    find_anagrams_helper(s, [], all_anagram, dic, len(s))
    return all_anagram


def find_anagrams_helper(s,  anagram, all_anagrams, dictionary, len_s):
    if len_s == len(anagram):
        if ''.join(anagram) in dictionary and ''.join(anagram) not in all_anagrams:
            all_anagrams.append(''.join(anagram))
            print('Found:', ''.join(anagram))
            print('Searching...')
    else:
        for i in range(len(s)):
            # choose
            anagram.append(s[i])
            # explore
            find_anagrams_helper(s[:i]+s[i+1:], anagram, all_anagrams, dictionary, len_s)
            # un-choose
            anagram.pop()


def has_prefix(sub_s, dic):
    """
    :param sub_s: str
    :return: Boolean
    """
    for vocab in dic:
        if vocab.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
