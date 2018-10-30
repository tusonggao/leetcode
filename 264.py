class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """       
        ugly_nums_list = [1]
        ugly_nums_seen = set([1])
        i, j, k = 0, 0, 0
        while len(ugly_nums_list)<n:
            n_2, n_3, n_5 = ugly_nums_list[i]*2, ugly_nums_list[j]*3, ugly_nums_list[k]*5
            num = min(n_2, n_3, n_5)
            if num==n_2:
                i += 1
            elif num==n_3:
                j += 1
            elif num==n_5:
                k += 1
            if num not in ugly_nums_seen:
                ugly_nums_list.append(num)
                ugly_nums_seen.add(num)
                
        return ugly_nums_list[-1]
        
        