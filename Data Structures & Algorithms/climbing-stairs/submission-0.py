class Solution:
    def climbStairs(self, n: int, cache = {}) -> int:
        if (n in cache):
            return cache[n]
        if (n ==1 or n ==2):
            return n
        cache[n] = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)
        return cache[n]