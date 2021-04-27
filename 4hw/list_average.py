def list_average():
    new_list = []
    total = 0
    average = 0
    elements = int(input("How many numbers do you want in the list: "))

    #create list
    for i in range(elements):
        element = int(input("Enter a number to add: "))
        new_list.append(element)

    #calculate average
    for i in new_list:
        total += i
    average = total / elements
    print(f"The average is {average}")

    return average

list_average()