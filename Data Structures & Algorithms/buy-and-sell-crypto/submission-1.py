class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r =0
        mx = 0
        while (r < len(prices)):
            if (prices[r] > prices[l]):
                mx = max((prices[r] - prices[l]), mx)
            else:
                l = r
            r += 1
        return mx