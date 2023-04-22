class Solution:
    def is_capital_letter(self,c:str):
        return True if 65<=ord(c)<=90 else False
    
    def minWindow(self, s: str, t: str) -> str:
        # we use prefix_sum sum

        # 1. loop through t, and count occurences of unique characters in t
        t_count=[0]*52
        for c in t:
            if self.is_capital_letter(c ):
                t_count[ord(c)-65]+=1
            else:
                t_count[ord(c)-97]+=1
        # check edge case where len(t)==1:
        if len(t)==1:
            if s.find(t[0])>-1:
                return t[0]
            else:return ""
        
        # 2.loop through s, and count occurences of unique characters in t
        s_sum=[]# s_sum[i]=a dict, counting the sum of occurences of each key in t_count
            
        for i in range(len(s)):
            if i==0:
                curr_dict=[0]*52
                for k in t_count:
                    curr_dict[k]=0
            else:
                curr_dict=dict(s_sum[i-1] )# copy last dict
            if t_count.get(s[i])!=None:
                curr_dict[s[i]]+=1
            s_sum.append(curr_dict)
       
        # check edge case where s does not have all chars of t
        last_prefix_sum= s_sum[len(s)-1]
        for k in last_prefix_sum:
            if last_prefix_sum[k]<t_count[k]:return ""
        
        
        
        # 3 move the sliding window of size len(t_count) accross and check conditions
        sliding_window_size=len(t_count)
        win_condition=sliding_window_size
        
        res=s
        # sliding_window[start_index:end_index]=s[start_index,end_index)
        for start_index in range(0,len(s)):
            for end_index in range(start_index+sliding_window_size,len(s)+1):
                
                # get occurences of each key in t_count
              
                curr_streak=0 # if win_condition==len(t_count.keys)
                too_small=False
                for k in t_count:
                    if start_index==0:
                        occurrences_for_this_char=s_sum[end_index-1][k]
                    else:#start_index>=1:
                        occurrences_for_this_char=s_sum[end_index-1][k]-s_sum[start_index-1][k]
                    if occurrences_for_this_char<t_count[k]:
                        too_small=True
                        break
                    elif occurrences_for_this_char>=t_count[k]:
                        curr_streak+=1
                if too_small:continue
                if curr_streak==win_condition:
                    if end_index-start_index<len(res):
                        res=s[start_index:end_index] 
                    if end_index-start_index == sliding_window_size:
                        return s[start_index:end_index]
                    
        return res
    def minWindow_tle(self, s: str, t: str) -> str:
        # we use prefix_sum sum

        # 1. loop through t, and count occurences of unique characters in t
        t_count=dict()
        for c in t:
            if t_count.get(c)==None:
                t_count[c]=1
            else:
                t_count[c]+=1
        # check edge case where len(t)==1:
        if len(t)==1:
            if s.find(t[0])>-1:
                return t[0]
            else:return ""
        
        # 2.loop through s, and count occurences of unique characters in t
        s_sum=[]# s_sum[i]=a dict, counting the sum of occurences of each key in t_count
            
        for i in range(len(s)):
            if i==0:
                curr_dict=dict()
                for k in t_count:
                    curr_dict[k]=0
            else:
                curr_dict=dict(s_sum[i-1] )# copy last dict
            if t_count.get(s[i])!=None:
                curr_dict[s[i]]+=1
            s_sum.append(curr_dict)
       
        # check edge case where s does not have all chars of t
        last_prefix_sum= s_sum[len(s)-1]
        for k in last_prefix_sum:
            if last_prefix_sum[k]<t_count[k]:return ""
        
        
        
        # 3 move the sliding window of size len(t_count) accross and check conditions
        sliding_window_size=len(t_count)
        win_condition=sliding_window_size
        
        res=s
        # sliding_window[start_index:end_index]=s[start_index,end_index)
        for start_index in range(0,len(s)):
            for end_index in range(start_index+sliding_window_size,len(s)+1):
                
                # get occurences of each key in t_count
              
                curr_streak=0 # if win_condition==len(t_count.keys)
                too_small=False
                for k in t_count:
                    if start_index==0:
                        occurrences_for_this_char=s_sum[end_index-1][k]
                    else:#start_index>=1:
                        occurrences_for_this_char=s_sum[end_index-1][k]-s_sum[start_index-1][k]
                    if occurrences_for_this_char<t_count[k]:
                        too_small=True
                        break
                    elif occurrences_for_this_char>=t_count[k]:
                        curr_streak+=1
                if too_small:continue
                if curr_streak==win_condition:
                    if end_index-start_index<len(res):
                        res=s[start_index:end_index] 
                    if end_index-start_index == sliding_window_size:
                        return s[start_index:end_index]
                    
        return res
               


if __name__ == "__main__":

    s = Solution()

    input1 = "rriswzrehwhvhbrzwkkogeuxsvfsipmzjwthxllfjtcsutrtfbhmidlcyruiiihrgdzdqkkzfnrcilvomecwjnyiguqpcaikdhovuaubnndyyyoleqhofiymcqdfqlpvvfqpgmqvawvywjlbbvrhdpvhfymyletglmxtyqpamkzkumlvhcemrzuzzixnoqvaevtflifzvejrrxoabtnvuhuwprjejgeobztokynffzyyymyzhluesoakflortuhvtclfabkhakfaxgzgrukmkmwszmjtgqqbubhucteeeledrejjawvkitckfnfnfvqzwxwbtcfznmcfqnqsjncughenwjaegqdeqbfldnktzmyrbojldnhjwnytyyzeqckigstlfdegrcztsigxxpgucepceoixssfakbmreqxyvytpibngqvcucrwihefbwncjooaugasbynthoinedryhkwqraxsxkwiamivtipwjdpqrxfwdywkitcztatsmsanelixvxweclwuldsqbocjhfkdhgxtyagclqciqynsllmyrgouvreeyqjfwhywjhbwxdepdtkofynyfdsauygspqznzykifleeqiwtcghjewhjazjwysrpiqchqorvzvcrfakjguskqzusbfp"
    input2 = "zxgohysqphhm"
    excepted = "ogeuxsvfsipmzjwthxllfjtcsutrtfbhmidlcyruiiihrgdzdq"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "aaaaaaaaaaaabbbbbcdd"
    input2 = "abcdd"
    excepted = "abbbbbcdd"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "abc"
    input2 = "bc"
    excepted = "bc"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "aa"
    input2 = "aa"
    excepted = "aa"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "ADOBECODEBANC"
    input2 = "ABC"
    excepted = "BANC"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "a"
    input2 = "a"
    excepted = "a"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "a"
    input2 = "aa"
    excepted = ""
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)
