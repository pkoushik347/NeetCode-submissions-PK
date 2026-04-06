class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        xorr = 0
        # print(xorr)
        for i in range(n):
            xorr ^= i
            # print(xorr)
            xorr ^= nums[i]
            # print(xorr)
        # print(xorr)
        return xorr ^n