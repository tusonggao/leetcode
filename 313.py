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
		
#解法二：使用堆队列，速度快

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        
        heap, uglies, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in range(1, n):
            uglies[i], k = heapq.heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]
                    