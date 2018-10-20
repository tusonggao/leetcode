class Solution(object):
    def init(self):
	    return
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []
        
        outcome = {}     
        
        for i in range(target+1):
            outcome[i] = []
            
        self.outcome[len(candidates)] = {}
        for j in range(target//candidates[-1]+1):
                self.outcome[len(candidates)][j*candidates[i]] = [candidates[-1]]*j
                
        for i in range(len(candidates)-1, -1, -1):
            self.outcome[i] = {}
            for j in range(1, target//candidates[i]+1):
                for i in range(target+1-j*candidates[i]):
                    self.outcome[i+j*candidates[i]] = [candidates[i]]*j + self.outcome[i]
                

        return self.outcome[target]
            
			
class Solution(object):
    def combinationSum(self, candidates, target):
        import copy
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []
        
        outcome, outcome_newest = {}, {}
        
        outcome[0] = [[]]
        for i in range(1, target+1):
            outcome[i] = []
                
        for i in range(len(candidates)-1, -1, -1):
            outcome_newest = copy.deepcopy(outcome)
            self.outcome[i] = {}
            for j in range(1, target//candidates[i]+1):
                for i in range(target+1-j*candidates[i]):                        
                    outcome_newest[i+j*candidates[i]] = [[candidates[i]]*j + lll for lll in outcome[i]]
            outcome = outcome_newest

        return outcome[target]
        