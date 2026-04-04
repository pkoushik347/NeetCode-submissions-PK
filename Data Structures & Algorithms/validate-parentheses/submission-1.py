class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in mp:
                if not stack:
                    return False
                elif stack[-1] != mp[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0