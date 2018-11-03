class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_positive = True if x > 0 else False
        x = x if x > 0 else -x
        
        num = 0        
        while(x):
            num = num*10 + x%10
            x //= 10
            if num >= 2**31: #overflow, return 0
                return 0
            
        return num if is_positive else -num