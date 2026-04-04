class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums[1:]:
            if ans > i:
                return i
        return ans