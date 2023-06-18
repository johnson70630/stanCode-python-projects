"""
File: similarity.py (extension)
Name: Johnson
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will compare short sequence DNA with long sequence DNA,
    and find the best match homology.
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    short_sequence = input("what DNA sequence would you like to match? ")
    ll = long_sequence.upper()
    ss = short_sequence.upper()
    best_dna = ""
    former = 0
    for i in range(len(ll)-len(ss)+1):
        dna = ""
        match_rate = 0
        for j in range(len(ss)):
            if ss[j] == ll[i+j]:
                match_rate += 1
                dna += ll[i+j]
            else:
                dna += ll[i+j]
        if match_rate >= former:
            best_dna = dna
            former = match_rate
    print("The best match is "+best_dna)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
