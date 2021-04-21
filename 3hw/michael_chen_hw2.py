import sys
import math

def main():
	#error handle wrong command-line argument count-
	if(len(sys.argv) != 2):
		print(f"Correct Usage: {sys.argv[0]} <year #>")
		return 0

	#Check if each char of the string is a number
	for i in range(len(sys.argv[1])):
		if sys.argv[1][i] < '0' or sys.argv[1][i] > '9':
			print("Error: The number you enter must be an integer")
			return 0

	#get the number from the command line and set a bool
	number = int(sys.argv[1])
	leap = " not"
		
	#check if the year is a leap year
	if number % 4 == 0:
		if number % 400.0 == 0:
			leap = ""
		else:
			if not (number % 100.0 == 0):
				leap = ""

	#print result
	print(f"{number} is{leap} a leap year")
	return 0;

main()