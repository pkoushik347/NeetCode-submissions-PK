class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # return s == s[::-1]
        st = ''
        for i in s:
            if (i.isalpha() or i.isdigit()):
                st += i.lower()
        # print(st)
        return st == st[::-1]
        
