import sys
import math

def main():
	#error handle wrong command-line argument count-
	if(len(sys.argv) != 2):
		print(f"Correct Usage: {sys.argv[0]} <year #>")
		return 0

	#get the number from the command line
	number = int(sys.argv[1])

	#conditional for results
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