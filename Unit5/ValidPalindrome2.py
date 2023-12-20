class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        skip = 1
        left = 0
        right = len(s) - 1


        return self.recursiveFunction(s, left,right,skip)

    def recursiveFunction(self, s, left, right, skip):
        if skip < 0:
            return False
        elif left > right:
            return True

        else:
            if  s[left] == s[right]:
                return self.recursiveFunction(s, left + 1, right - 1, skip)
            else:
                return self.recursiveFunction(s, left + 1, right, skip - 1) or self.recursiveFunction(s, left, right-1, skip - 1)

                    
                            

        

s = "aba"
s1 = Solution()
print(s1.validPalindrome(s))