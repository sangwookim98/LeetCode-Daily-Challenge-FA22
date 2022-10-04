class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        
        # using lists
        a = list(a)
        b = list(b)
        
       # removing all bits from the back
        # while loop goes through bit by bit
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            
            # floor division by 2 since theres 0 and 1
            carry //= 2
        # result has to be reversed since pop 
        return result[::-1]        
