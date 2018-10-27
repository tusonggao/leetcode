#使用O(n)空间的解法1

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(set(nums)) * 3
        ans = (s - sum(nums))//2
        return ans

#使用O(n)空间的解法2		

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        for val, num in counter.items():
            if num != 3:
                return val
				
				
#使用O(1)空间的解法1

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            count = 0
            for j in nums:
                count += (j>>i) & 1
            count %= 3
            result |= count<<i
        return int(result)
        