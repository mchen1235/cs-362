def list_average(new_list):
    total = 0
    average = 0

    #calculate average
    for i in new_list:
        total += i
    average = total / len(new_list)

    return average