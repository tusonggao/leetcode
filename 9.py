class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_str_r = x_str[::-1]
        
        return x_str==x_str_r
        
        
