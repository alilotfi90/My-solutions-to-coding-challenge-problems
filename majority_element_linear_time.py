def majorityElement(array):
    lis = array

    cur = 0
    candindex = cur

    counter = {}
    counter[candindex] = 0

    while cur < len(lis):

        # update counter
        if lis[cur] == lis[candindex]:
            counter[candindex] += 1
        else:
            counter[candindex] -= 1

        # check if we reached a position where we can restart thereafter
        if counter[candindex] == 0:
            candindex = cur + 1
            counter[candindex] = 0

        cur += 1

    return lis[candindex]
