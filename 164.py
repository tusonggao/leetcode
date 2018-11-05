class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        
        nums = sorted(nums)
        max_gap = float('-inf')
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
            
        return max_gap
        