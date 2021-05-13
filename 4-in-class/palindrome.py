def palindrome(word):
    length = len(word)

    for i in range(int(length/2)):
        if not (word[i] == word[length - 1 - i]):
            return False

    return True