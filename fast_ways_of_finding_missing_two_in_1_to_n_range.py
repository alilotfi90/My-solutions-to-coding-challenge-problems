def missingNumbers(nums):
    n = len(nums) + 2

    sum_of_two_missing = n * (n + 1) // 2 - sum(nums)

    print(sum_of_two_missing)

    avg_of_two = sum_of_two_missing // 2

    sum_left_half = 0
    sum_right_half = 0
    for a in nums:
        if a <= avg_of_two:
            sum_left_half += a
        else:
            sum_right_half += a

    missing_left = (avg_of_two * (avg_of_two + 1) // 2) - sum_left_half
    missing_right = (n * (n + 1) // 2 - avg_of_two * (avg_of_two + 1) // 2) - sum_right_half

    return [missing_left, missing_right]
