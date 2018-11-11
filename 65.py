class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            v = float(s)
        except:
            return False
        return True
