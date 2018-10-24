class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not hasattr(self, 'outcome'):
            self.outcome = {0: [], 1: ['()']}
            
        if n in self.outcome:
            return self.outcome[n]            
            
        outcome_list_sum = []
        for inner_n in range(0, n):
            outcome_list_inner = self.generateParenthesis(inner_n)
            outcome_list_right = self.generateParenthesis(n-1-inner_n)
            outcome_list = ['(']
            
            if len(outcome_list_inner)>0:
                outcome_list = ['(' + ss for ss in outcome_list_inner]
                    
            outcome_list = [s + ')' for s in outcome_list]
            
            if len(outcome_list_right)>0:
                outcome_list = [ss1 + ss2 for ss1 in outcome_list 
                                          for ss2 in outcome_list_right]
                        
            outcome_list_sum += outcome_list
        
        self.outcome[n] = outcome_list_sum
        return self.outcome[n]
                
            
            
            
        