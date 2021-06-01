def target_sum(array, target):
    result = []
    ptr1 = 0
    ptr2 = 1
    array.sort()
    
    #iterate through the array
    while len(result) == 0:
        val1 = array[ptr1]
        val2 = array[ptr2]
        total = val1 + val2

        #valid ptrs
        if total == target:
            result.append(val1)
            result.append(val2)
        #too small
        elif total < target:
            #ptrs next to each other
            if ptr2 == ptr1 + 1:
                ptr2 += 1
            #ptrs not next to each other
            else:
                ptr1 += 1
        #too large
        else:
            ptr1 -= 1

    return result
