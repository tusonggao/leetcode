class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        digits_now = str(bin(n))[2:]
        zeros_num = 32 - len(digits_now)        
        return int(''.join(reversed('0'*zeros_num + digits_now)), 2)