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
		

# 另外一种divide and conquer的递归解法，为了扩充思路

class Solution:
    def maxSubArray_worker(self, nums, start_idx, end_idx):
        if start_idx>end_idx:
            return float('-inf')
        if start_idx==end_idx:
            return nums[start_idx]
        
        mid_idx = (start_idx + end_idx)//2
        max_subarray_left = self.maxSubArray_worker(nums, start_idx, mid_idx)
        max_subarray_right = self.maxSubArray_worker(nums, mid_idx+1, end_idx)
        
        max_sum_left = float('-inf')
        sum_continuous = 0
        for i in range(mid_idx, start_idx-1, -1):
            sum_continuous += nums[i]
            if max_sum_left < sum_continuous:
                max_sum_left = sum_continuous
        
        max_sum_right = float('-inf')
        sum_continuous = 0
        for i in range(mid_idx+1, end_idx+1):
            sum_continuous += nums[i]
            if max_sum_right < sum_continuous:
                max_sum_right = sum_continuous
                
        return max(max_subarray_left, max_subarray_right, 
                   max_sum_left + max_sum_right)        
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubArray_worker(nums, 0, len(nums)-1)
        
        




        