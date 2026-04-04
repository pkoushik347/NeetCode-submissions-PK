class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        longest = cur = 1

        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                cur += 1
            elif nums[i+1] != nums[i]:
                cur = 1
            longest = max(longest, cur)

        return longest