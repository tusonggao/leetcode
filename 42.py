class Solution:
    def trap_range(self, height, left_index, right_index):
        if left_index >= right_index:
            return 0
        if left_index==(right_index-1):
            return min(height[left_index], height[right_index])
        
        max_height = max(height[left_index:(right_index+1)])
        for i in range(left_index, right_index+1):
            if height[i]==max_height:
                max_index_left = i
                break
        for i in range(right_index, left_index-1, -1):
            if height[i]==max_height:
                max_index_right = i
                break
        
        max_height = -1
        max_index_left_next = max_index_left
        for i in range(max_index_left-1, left_index-1, -1):
            if height[i] >= max_height:
                max_index_left_next = i
                max_height = height[i]
        
        max_height = -1
        max_index_right_next = max_index_right
        for i in range(max_index_right+1, right_index+1):
            if height[i] >= max_height:
                max_index_right_next = i
                max_height = height[i]
                
        return ( (max_index_right - max_index_left)*max_height + 
                 (max_index_left - max_index_left_next)*min(height[max_index_left], height[max_index_left_next]) +
                 (max_index_right_next - max_index_right)*min(height[max_index_right_next], height[max_index_right]) +
                 self.trap_range(height, left_index, max_index_left_next) + 
                 self.trap_range(height, max_index_right_next, right_index) )
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.trap_range(height, 0, len(height)-1)