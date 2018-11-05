class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v_parts_1 = version1.split('.')
        v_parts_2 = version2.split('.')
        
        if len(v_parts_1) > len(v_parts_2):
            v_parts_2 += ['0']*(len(v_parts_1) - len(v_parts_2))
        elif len(v_parts_1) < len(v_parts_2):
            v_parts_1 += ['0']*(len(v_parts_2) - len(v_parts_1))
        
        for i in range(len(v_parts_1)):
            if int(v_parts_1[i]) > int(v_parts_2[i]):
                return 1
            elif int(v_parts_1[i]) < int(v_parts_2[i]):
                return -1
        return 0
        