"""
File: extension1_factorial.py
Name: Johnson
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	print("Welcome to stanCode factorial master")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))
		if n == EXIT:
			print("- - - - - See ya! - - - - -")
			break
		else:
			ans = n
			while True:
				if n == 1:
					print("Answer: "+str(ans))
					break
				else:
					n -= 1
					ans *= n


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
