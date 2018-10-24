class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_brackets = ['(', '[', '{']
        right_brackets = [')', ']', '}']
        stack_list = ['x'] #stub character
        for c in s:
            if c in left_brackets:
                stack_list.append(c)
            else:
                right_idx = right_brackets.index(c)
                if stack_list[-1]==left_brackets[right_idx]:
                    stack_list.pop()
                else:
                    return False
        if len(stack_list)==1:
            return True
        else:
            return False