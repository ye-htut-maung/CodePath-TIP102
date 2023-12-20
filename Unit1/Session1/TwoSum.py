class Solution:
    def twoSum(self, nums: list, target: int):
     for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return [i, j]
        
    

nums = [3,3]
target = 6

s1 = Solution()
print(s1.twoSum(nums, target))

