#解法一： 不使用正则表达式匹配的方法 
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str)==0:
            return 0
        
        is_pos = True        
        if str[0] in ('+', '-'):
            if str[0]=='-':
                is_pos = False
            str = str[1:]
            if len(str)==0:
                return 0
            
        num_str = ''
        for i in range(len(str)):
            if str[i]>='0' and str[i]<='9':
                num_str += str[i]
            else:
                break
        
        if len(num_str)==0:
            return 0
        
        num = int(num_str)
        if is_pos:
            if num>=2**31-1:
                return 2**31-1
            else:
                return num
        else:
            if num>=2**31:
                return -2**31
            else:
                return -num
            
        