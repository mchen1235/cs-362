def leap_year(number):
	#check if the year is a leap year
	if number % 4 == 0:
		if number % 400.0 == 0:
			return True
		else:
			if number % 100.0 == 0:
				return False
			return True

	return False

leap_year(400)