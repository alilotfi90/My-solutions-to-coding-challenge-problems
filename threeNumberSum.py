def threeNumberSum(array, target):
    array.sort()
    retlis = []

    midind = 1
    while midind >= 1 and midind <= len(array) - 2:

        # we fix mindind
        leftind = midind - 1
        rightind = midind + 1
        while leftind >= 0 and rightind <= len(array) - 1 and leftind < midind and midind < rightind:
            if array[leftind] + array[midind] + array[rightind] - target == 0:

                retlis.append([array[leftind], array[midind], array[rightind]])
                leftind -= 1
                rightind += 1
            elif array[leftind] + array[midind] + array[rightind] - target > 0:
                print(array[leftind], array[midind], array[rightind])
                leftind -= 1

            else:
                rightind += 1

        midind += 1

    retlis.sort()
    return retlis