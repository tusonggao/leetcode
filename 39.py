class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def combination(index, tar):
            if tar == 0:
                return [[]]
            
            if tar < candidates[index]:
                return []
            
            ans = []
            for i in range(index, len(candidates)):
                res = combination(i, tar - candidates[i])
                ans.extend([[candidates[i]] + item for item in res])
            
            return ans
        
        
        candidates = sorted(candidates)
        return combination(0, target)