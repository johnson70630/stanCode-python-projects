"""
File: complement.py
Name: Johnson
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will find DNA complement.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    param dna: The DNA to be complement
    return result: The complemented DNA
    """
    if not dna.isalpha():
        return "DNA strand is missing"
    else:
        com = ""
        for i in range(len(dna)):
            if dna[i] == 'A':
                com += 'T'
            elif dna[i] == 'T':
                com += 'A'
            elif dna[i] == 'C':
                com += 'G'
            else:
                com += 'C'
        return com


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
