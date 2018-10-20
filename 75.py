class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_0 = nums.count(0)
        num_1 = nums.count(1)
        
        for i in range(num_0):
            nums[i] = 0
        for i in range(num_0, num_0+num_1):
            nums[i] = 1
        for i in range(num_0+num_1, len(nums)):
            nums[i] = 2
        return