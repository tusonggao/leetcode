class Solution:    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        i_start = 0     # 最长回文串起始位置
        max_len = 0     # 最长回文串长度
        
        # 思路：
		# i作为回文字符的最后一个字符位置，完整遍历整个字符串s
        # max_len一定会从1开始变大到最大可以取到的值

        for i in range(len(s)): # i 代表最长字符串最后一个字符的位置
            if (i-max_len-1)>=0 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:
                i_start = i - max_len -1
                max_len += 2
            elif (i-max_len)>=0 and s[i-max_len:i+1]==s[i-max_len:i+1][::-1]:
                i_start = i - max_len
                max_len += 1
        return s[i_start: i_start+max_len]
        