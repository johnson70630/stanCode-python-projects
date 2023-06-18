"""
File: caesar.py
Name: Johnson
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program is Caesar Cipher.
    """
    sn = int(input("Secret number: "))
    cs = input("What's the ciphered string? ")
    print(new_alphabet(sn, cs))


def new_alphabet(sn, cs):
    ans = ""
    cs = cs.upper()
    for i in range(len(cs)):
        if cs[i].isalpha():
            if ALPHABET.find(cs[i])+sn < len(ALPHABET)-1:
                ans += ALPHABET[ALPHABET.find(cs[i])+sn]
            else:
                ans += ALPHABET[ALPHABET.find(cs[i])+sn-len(ALPHABET)]
        else:
            ans += cs[i]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
