def full_name():
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    full = first + " " + last
    print(f"The full name is {full}")

    return full


full_name()