from collections import Counter

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_counter = Counter(A.split() + B.split())
        return [w for w in words_counter if words_counter[w]==1]