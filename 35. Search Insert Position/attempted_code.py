class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_list = 0
        right_list = len(nums) - 1
        
        # Binary Search
        
        while left_list <= right_list:
            # Creating given list's middle point index 
            mid_point = (left_list + right_list)/2
            
            # Checking location of target based on the halves of the list
            # Target is less than mid_point
            if nums[mid_point] < target:
                left_list = mid_point+1
                
            # Target is more than mid_point
            else:
                if (nums[mid_point] == target) and (nums[mid_point-1]) != target:
                    return mid_point
                else:
                    right_list = mid_point-1
        return l
        
