def end_zero_ind(array, begin):
    end = begin
    while end + 1 < len(array) and array[end + 1] == 0:
        end = end + 1
    return end


def bestSeat(seats):
    # Write your code here.
    checkind = 0
    max_len_to_sit = -1
    ind_to_sit = -1

    while checkind < len(seats):
        if seats[checkind] == 0:
            endind = end_zero_ind(seats, checkind)
            if endind - checkind > max_len_to_sit:
                ind_to_sit = (checkind + endind) // 2
                max_len_to_sit = endind - checkind
            checkind = endind + 1
        else:
            checkind += 1
    return ind_to_sit