class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pos] = nums[i]
                pos += 1
        return pos