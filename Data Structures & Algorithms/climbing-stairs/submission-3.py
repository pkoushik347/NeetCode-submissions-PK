class Solution:
    def climbStairs(self, n: int, cache = {}) -> int:
        if (n ==1 or n ==2):
            return n
        cache = [0] * (n +1)
        cache[2], cache[1] = 2, 1
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]