# 111
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_idx = {}
        for i in range(len(nums)):
            nums_idx[nums[i]] = i
        
        for i in range(len(nums)):
            val = target-nums[i]
            if val in nums_idx and nums_idx[val]!=i:
                return [i, nums_idx[val]]
        