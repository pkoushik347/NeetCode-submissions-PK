class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nn = (n * (n+1))//2
        return nn - sum(nums)