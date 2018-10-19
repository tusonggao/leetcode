class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        
        max_length = 1
        start_index, end_index = 0, 0
        
        for i in range(1, len(s)):
            s_index = s[start_index:end_index+1].find(s[i])
            end_index = i
            if s_index==-1:
                max_length = max(max_length, end_index-start_index+1)
            else:
                start_index += s_index + 1
                
        return max_length