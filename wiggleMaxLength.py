class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        dec = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = dec[i-1] + 1
                dec[i] = dec[i-1]
            elif nums[i] < nums[i-1]:
                dec[i] = inc[i-1] + 1
                inc[i] = inc[i-1]
            else:
                inc[i] = inc[i-1]
                dec[i] = dec[i-1]
        return max(max(inc), max(dec))
