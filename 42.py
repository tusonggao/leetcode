class Solution:
    def count_trap_volume(self, height, left_index, right_index):
        if (left_index + 1) >= right_index:
            return 0
        return ((right_index-left_index-1)*min(height[left_index], height[right_index]) -
                 sum(height[left_index+1:right_index]))
        
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=1:
            return 0
        
        trap_sum = 0        
        max_height = max(height)
        for i in range(0, len(height)):
            if height[i]==max_height:
                max_index_left = i
                break
        for i in range(len(height)-1, -1, -1):
            if height[i]==max_height:
                max_index_right = i
                break
        
        trap_sum += self.count_trap_volume(height, max_index_left, max_index_right)
        
        current_max_height = height[0]
        left_index = 0
        cost_sum = height[0]
        for i in range(1, max_index_left+1):
            if current_max_height <= height[i]:
                current_max_height = height[i]
                right_index = i
                trap_sum += self.count_trap_volume(height, left_index, right_index)
                left_index = right_index
        
        current_max_height = height[-1]
        right_index = len(height)-1
        for i in range(len(height)-2, max_index_right-1, -1):
            if current_max_height <= height[i]:
                current_max_height = height[i]
                left_index = i
                trap_sum += self.count_trap_volume(height, left_index, right_index)
                right_index = left_index
                
        return trap_sum
    