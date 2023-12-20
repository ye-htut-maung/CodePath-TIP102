class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        frequency = dict()
        for i in arr:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        print(frequency)
        numSet = set()
        for i in frequency.values():
            if i not in numSet:
                numSet.add(i)
            else:
                return False
        return True
        
# O(n)


arr = [1,2,2,1,1,3]
s1 = Solution()
print(s1.uniqueOccurrences(arr))