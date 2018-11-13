class Solution:
    def __init__(self):
        self.cache = {}
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        
        if len(s)==0:
            if len(p)==0:
                self.cache[(s, p)] = True
                return True
            elif ('a' <= p[0] <= 'z' or p[0]=='.') and len(p)>=2 and p[1]=='*':
                self.cache[(s, p)] = self.isMatch(s, p[2:])
                return self.cache[(s, p)]
            else:
                self.cache[(s, p)] = False
                return False
        
        if len(p)==0:
            self.cache[(s, p)] = False
            return False
        
        if 'a' <= p[0] <= 'z':
            if s[0]!=p[0]:
                if len(p)>=2 and p[1]=='*':
                    self.cache[(s, p)] = self.isMatch(s, p[2:])
                else:
                    self.cache[(s, p)] = False
            else:
                if len(p)>=2 and p[1]=='*':
                    self.cache[(s, p)] = self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    self.cache[(s, p)] = self.isMatch(s[1:], p[1:])
        elif p[0]=='.':
            if len(p)>=2 and p[1]=='*':
                self.cache[(s, p)] = self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.cache[(s, p)] = self.isMatch(s[1:], p[1:])
        else:
            self.cache[(s, p)] = False
        
        return self.cache[(s, p)]
        
        
            
        
        
        
        
        
            
        