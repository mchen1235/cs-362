def reverse(string):
    result = ""
    word_list = [""]
    word_num = 0
    period = False

    if len(string) == 0:
        return ""

    #set period bool
    if string[len(string)-1] == ".":
        period = True

    #separate the list by wo
    for letter in string:
        if letter == " ":
            word_list.append("")
            word_num += 1
        else:
            word_list[word_num] += letter

    #remove the period
    if period:
        word_list[word_num] = word_list[word_num][0:len(word_list[word_num]) - 1]

    #create the new sentence
    while word_num >= 0:
        result += word_list[word_num]
        if word_num >= 1:
            result += " "
        word_num -= 1

    #add the period
    if period:
        result += "."

    return result