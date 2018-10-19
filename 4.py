class Solution:
    def array_median_num(self, nums, start_index, end_index):
        nums_len = end_index - start_index + 1
        if nums_len%2==1:
            return nums[int((start_index + end_index)/2)]
        else:
            return (nums[int((start_index + end_index + 1)/2-1)] + 
                    nums[int((start_index + end_index + 1)/2)]) / 2
            
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==0:
            return self.array_median_num(nums2, 0, len(nums2)-1)
        if len(nums2)==0:
            return self.array_median_num(nums1, 0, len(nums1)-1)
        
        low_index_1, high_index_1 = 0, len(nums1)-1
        low_index_2, high_index_2 = 0, len(nums2)-1
        
        while True:
            if low_index_1 > high_index_1:
                return self.array_median_num(nums2, low_index_2, high_index_2)
            if low_index_2 > high_index_2:
                return self.array_median_num(nums1, low_index_1, high_index_1)
            if low_index_1==high_index_1 and low_index_2==high_index_2:
                return (nums1[low_index_1] + nums2[low_index_2])/2
            
            if nums1[low_index_1] < nums2[low_index_2]:
                low_index_1 += 1
            else:
                low_index_2 += 1
            if nums1[high_index_1] < nums2[high_index_2]:
                high_index_2 -= 1
            else:
                high_index_1 -= 1
                
                
            
                
        