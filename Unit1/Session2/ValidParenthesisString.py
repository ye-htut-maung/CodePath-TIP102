from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) == 1 or len(s) == 0:
            return False
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if (prev == "(" and i == ")") or (prev == "{" and i == "}") or (prev == "[" and i == "]"):
                    pass
                else:
                    return False

        if(len(stack) == 0):
            return True
        else:
            return False






s = Solution()
s.isValid()