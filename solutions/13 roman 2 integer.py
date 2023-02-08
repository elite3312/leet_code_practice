class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        #print(symbols)
        '''I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.'''
        sum=0
        for i in range(len(s)):
            if(i+1<len(s)):
                match(s[i:i+2]):
                    case ('IV'):
                        sum-=1
                    case ('IX'):
                        sum-=1
                    case ('XL'):
                        sum-=10
                    case ('XC'):
                        sum-=10
                    case ('CD'):
                        sum-=100
                    case ('CM'):
                        sum-=100    
                    case _:
                        sum+=symbols_dict[s[i]]
            else:
                sum+=symbols_dict[s[i]]
        return sum
            
#s = "III"
s="MCMXCIV"#1994
#1000-100+1000-10+100-1+5
print(Solution().romanToInt(s))
