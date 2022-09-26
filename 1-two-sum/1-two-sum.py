class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_check = {}
        
        for i in range(len(nums)):
            second_add = target - nums[i]
            if second_add in sum_check:
                return [sum_check[second_add], i]
            else:
                sum_check[nums[i]] = i
        