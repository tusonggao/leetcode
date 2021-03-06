class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        outcome_list_of_list = []
        for i in range(numRows):
            outcome_list_of_list.append([])
        
        direction = 1
        current_row = 0
        step_num = 0
        for c in s:
            outcome_list_of_list[current_row].append(c)
            current_row += direction
            step_num += 1
            if step_num%(numRows-1)==0:
                direction *= -1
        
        outcome_s = ''
        for i in range(numRows):
            outcome_s += ''.join(outcome_list_of_list[i])
        return outcome_s
            
            
            
        