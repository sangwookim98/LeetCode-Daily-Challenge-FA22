class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Setup for list 
        count = [0] * 102
        for num in nums:
            count[num+1] += 1

        # seeing how many each number has smaller number than itself
        for i in range(1, 102):
            count[i] += count[i-1]

        result = [count[num] for num in nums]        
        return result