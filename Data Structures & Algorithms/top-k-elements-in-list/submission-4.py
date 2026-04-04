class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dc = {}
        # ans = set()
        for i in nums:
            # if ():
            dc[i] = dc.get(i, 0) + 1
            # if (dc[i] >= k):
            #     ans.add(i)
        # return list(ans)
        sorted_d = dict(sorted(dc.items(), key=lambda x: x[1])[::-1])
        return list(sorted_d.keys())[:k]
