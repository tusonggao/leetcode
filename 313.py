#解法一：模型leetcode 264的解法，但是速度比较慢

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_nums = [1]
        primes_num = len(primes)
        primes_idx = [0]*primes_num
        
        while len(ugly_nums)<n:
            num_min = 10**50
            for i in range(primes_num):
                num_min = min(num_min, ugly_nums[primes_idx[i]]*primes[i])
            for i in range(primes_num):
                if num_min==ugly_nums[primes_idx[i]]*primes[i]:
                    primes_idx[i] += 1
            ugly_nums.append(num_min)
        return ugly_nums[-1]
		
#解法二：模型leetcode 264的解法，但是速度比较慢
                    