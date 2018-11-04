class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zero_num = 0
        while n:
            zero_num += n//5
            n //= 5
        return zero_num