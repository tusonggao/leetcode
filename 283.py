class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current_idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[current_idx] = nums[i]
                current_idx += 1
        for i in range(current_idx, len(nums)):
            nums[i] = 0
        return