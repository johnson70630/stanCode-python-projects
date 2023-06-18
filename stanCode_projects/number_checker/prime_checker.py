"""
File: prime_checker.py
Name: Johnson
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100  # Sentinel Value


def main():
	print("Welcome to the prime checker!")
	while True:
		n = int(input("n: "))
		if n == EXIT:
			print("Have a good one!")
			break
		else:
			x = 2
			while True:
				if n == x:
					print(str(n)+" is a prime number")
					break
				elif n % x == 0:
					print(str(n) + " is not a prime number.")
					break
				else:
					x += 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
