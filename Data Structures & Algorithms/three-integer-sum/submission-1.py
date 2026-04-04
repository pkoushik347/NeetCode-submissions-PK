class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(0, n-2):
            l,r = i+1, n-1
            while (l < r):
                s = nums[i] + nums[l] + nums[r]
                if (s == 0):
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif (s < 0):
                    l += 1
                else:
                    r -= 1
        return [list(t) for t in res]