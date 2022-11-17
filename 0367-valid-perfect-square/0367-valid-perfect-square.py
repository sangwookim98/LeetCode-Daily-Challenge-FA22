class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
#         left_end = 0
#         right_end = num
        
#         while left_end <= right_end:
#             midpoint = left_end + (right_end - left_end)
            
#             if midpoint ** 2 == num:
#                 return True
            
#             elif midpoint ** 2 > num:
#                 right_end = midpoint - 1
                
#             else:
#                 left_end = midpoint + 1
                
                
#         return False

        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False