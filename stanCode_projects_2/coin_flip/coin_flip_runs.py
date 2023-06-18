"""
File: coin_flip_runs.py
Name: Johnson
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program shows flips of a coin that match the input number of runs.
	"""
	print("Let's flip a coin!")
	n = int(input("Number of runs: "))
	flips = ""
	runs = 0
	is_in_a_row = False
	coin1 = r.randrange(0, 2)
	if coin1 == 0:
		flips += "H"
	else:
		flips += "T"
	while True:
		coin2 = r.randrange(0, 2)
		if coin2 == 0:
			flips += "H"
		else:
			flips += "T"
		if coin2 == coin1:
			if not is_in_a_row:
				runs += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		coin1 = coin2
		if n == runs:
			print(flips)
			break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
