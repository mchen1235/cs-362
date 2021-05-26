def fizzbuzz(num):
    string = ""

    if int(num) < 1:
        return string

    for i in range(1, int(num) + 1):
        if int(i) % 3 == 0:
            string += "Fizz "
        elif int(i) % 5 == 0:
            string += "Buzz "
        else:
            string += str(i)
            string += " "

    return string