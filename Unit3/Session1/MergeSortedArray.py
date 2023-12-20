class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1, -1, -1):
            if (nums1[i] == 0) :
                nums1.pop()
        if m == 0:
            nums1.extend(nums2)
        if n == 0:
            return
        else:
            i = 0
            j = 0

            while (i < m and j < n):
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    j += 1
                    i += 1
                else:                   
                    i += 1
                print(i,j)

                print(nums1)
            
            if i == m and m != 0:
                i = 0
                for k in range(j, len(nums2)):
                    if nums1[i] >= nums2[k]:
                        nums1.insert(i, nums2[k])
                        i += 1
                    else:
                        nums1.append(nums2[k])
                        i += 1




nums1 = [1,0]
m = 1
nums2 = [2]
n = 1
s1 = Solution()
s1.merge(nums1, m, nums2, n)

print(nums1)