def fizzbuzz(num):
    string = ""

    if int(num) < 1:
        return string

    for i in range(1, int(num) + 1):
        if int(i) % 3 == 0:
            string += "Fizz "
        else:
            string += str(i)
            string += " "

    return string