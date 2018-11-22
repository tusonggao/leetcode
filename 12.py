class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = ''
        map_str = {  1: 'I',   2: 'II',   3: 'III',   4: 'IV',   5: 'V',   6: 'VI',   7: 'VII',   8: 'VIII',   9: 'IX', 
                    10: 'X',  20: 'XX',  30: 'XXX',  40: 'XL',  50: 'L',  60: 'LX',  70: 'LXX',  80: 'LXXX',  90: 'XC', 
                   100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM' 
                  }
        
        num_str += 'M'*(num//1000)
        num %= 1000
        
        if num//100>0:
            num_str += map_str[(num//100)*100]
        num %= 100
        
        if num//10>0:
            num_str += map_str[(num//10)*10]
        num %= 10
        
        if num>0:
            num_str += map_str[num]            
            
        return num_str
		
		
#################################################################################
###another solution:

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                "V", "IV", "I"]
        i=0
        roman = ''
        while(num!=0):
            if(num>=base[i]):
                num-=base[i]
                roman+=strs[i]
            else:
                i+=1
        return roman


        
        