class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mx = 0
        for i in range(n):
            st = set()
            for j in range(i, n):
                if s[j] in st:
                    break
                st.add(s[j])
                mx = max(mx, j - i + 1)
            print(st)
        return mx