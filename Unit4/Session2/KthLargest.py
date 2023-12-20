import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        negative_nums = [-num for num in nums]
        negative_nums = [-num for num in nums]
        heapq.heapify(negative_nums)
        for _ in range(0, k):    
            ans = heapq.heappop(negative_nums)
        return -ans








nums = [3,2,1,5,6,4]
k = 2

s1 = Solution()
print(s1.findKthLargest(nums, k))