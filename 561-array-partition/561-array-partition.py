class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ascending order inside list
        nums.sort()
        
        listPair_sum = 0
        
        # every pair in the list of each element
        for i in range(0, len(nums), 2):
            listPair_sum += nums[i]
            
        return listPair_sum