"""
File: quadratic_solver.py
Name: Johnson
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	dcm = b*b-4*a*c
	if dcm < 0:
		print("No real roots")
	else:
		d = math.sqrt(dcm)
		x1 = (-b+d)/(2*a)
		x2 = (-b-d)/(2*a)
		if dcm > 0:
			print("Two roots: "+str(x1)+','+str(x2))
		else:
			print("One root: "+str(x1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
