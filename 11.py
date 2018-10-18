class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)
        left_index_arr, right_index_arr = [], []
        
        max_height = -1
        for i in range(len_height):
            if height[i]>max_height:
                left_index_arr.append(i)
                max_height = height[i]
        
        max_height = -1
        for i in range(len_height-1, 0, -1):
            if height[i]>max_height:
                right_index_arr.append(i)
                max_height = height[i]

        max_area = -1
        for left_index in left_index_arr:
            for right_index in right_index_arr:
                if left_index >= right_index:
                    continue
                else:
                    new_area = (right_index - left_index)*min(
                                  height[right_index], height[left_index])
                    max_area = max(max_area, new_area)
        return max_area