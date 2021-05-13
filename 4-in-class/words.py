def words(sentence):
    count = 0
    length = len(sentence)

    if length > 0:
        if not (sentence[0] == ' '):
            count += 1

        for i in range(len(sentence) - 1):
            if sentence[i] == ' ' and not (sentence[i + 1] == ' '):
                count += 1

    return count