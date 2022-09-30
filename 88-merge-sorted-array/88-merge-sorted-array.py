class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # m+n = length of new merged array - all results into nums1
        
        # Compare then Merge, compare the ending indexes, add from the back which are 0's
        #  0 1 2 3 4 5
        # [1,2,3,0,0,0] nums1
        # [2,5,6]       nums2
        
        # m = 3
        # n = 3
        
        while n > 0:
            # as long as it doesnt exceed first element of nums1
            # Checking for last element (first time comparison between nums1 and nums2
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                # to the next last element of nums2
                n -= 1
            else:
                # update to the next last element of nums1
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        
        