class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        now_sum = 0
        for n in nums:
            if (now_sum + n) > max_sum:
                max_sum = now_sum + n
            now_sum = (now_sum + n) if (now_sum + n) > 0 else 0
        return max_sum
        