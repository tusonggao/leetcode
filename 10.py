class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s)==0:
            if len(p)==0:
                return True
            elif ('a' <= p[0] <= 'z' or p[0]=='.') and len(p)==2 and p[1]=='*':
                return True
            else:
                return False
        
        if len(p)==0 and len(s)>0:
            return False
        
        if 'a' <= p[0] <= 'z':
            if s[0]!=p[0]:
                if len(p)>=2 and p[1]=='*':
                    return self.isMatch(s, p[2:])
                else:
                    return False
            else:
                if len(p)>=2 and p[1]=='*':
                    return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s[1:], p[1:])
        elif p[0]=='.':
            if len(p)>=2 and p[1]=='*':
                return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            return False
        
        
            
        
        
        
        
        
            
        