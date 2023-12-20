class Solution:
    def containsDuplicate(self, nums):
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False


nums = [1,1,1,3,3,4,3,2,4,2]

s1 = Solution()
print(s1.containsDuplicate(nums))