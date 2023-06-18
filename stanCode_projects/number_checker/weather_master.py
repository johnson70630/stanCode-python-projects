"""
File: weather_master.py
Name: Johnson
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1  # Sentinel Value


def main():
	print('stanCode "Weather Master 4.0"!')
	temp = int(input("Next Temperature: (or "+str(EXIT)+" to quit)? "))
	if temp == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = temp
		minimum = temp
		total = temp
		day = 1
		cold = 0
		if temp < 16:
			cold += 1
		while True:
			temp = int(input("Next Temperature: (or -100 to quit)? "))
			if temp == EXIT:
				break
			else:
				if temp > maximum:
					maximum = temp
				if temp < minimum:
					minimum = temp
				if temp < 16:
					cold += 1
				total += temp
				day += 1
		avg = total/day
		print("Highest temperature = "+str(maximum))
		print("Lowest Temperature = "+str(minimum))
		print("Average = "+str(avg))
		print(str(cold)+" cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
