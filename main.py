class Solution:
    def is_capital_letter(self,c:str):
        return True if 65<=ord(c)<=90 else False
    
    def access_hash_table(self,hash_table:list,c:str):
        if self.is_capital_letter(c):
            return hash_table[ord(c)-65]
        else:
            return hash_table[ord(c)-97+26]
    def update_hash_table(self,hash_table:list,c:str,add_value:int):
        if self.is_capital_letter(c):
            hash_table[ord(c)-65]+=add_value
        else:
            hash_table[ord(c)-97]+=add_value

    def minWindow(self, s: str, t: str) -> str:
        # we use prefix_sum sum

        # 1. loop through t, and count occurences of unique characters in t
        t_count=[0]*52# upper case*26+lower case*26 
        for c in t:
            self.update_hash_table(t_count,c,1)
        index_with_nonzero_elems_in_t_count=[]
        for i in range(52):
            if t_count[i]>0:
                
                index_with_nonzero_elems_in_t_count.append(i)
        
        # check edge case where len(t)==1:
        if len(index_with_nonzero_elems_in_t_count)==1:
            if s.find(t)>-1:
                return t
            else:return ""
        
        # 2.loop through s, and count occurences of characters in t
        s_sum=[]# s_sum[i]=accumulated the sum of occurences of each key in t_count from s[0] to s[i]
            
        for i in range(len(s)):
            if i==0:
                curr_dict=[0]*52

            else:
                curr_dict=s_sum[i-1].copy()# copy last dict
            if self.access_hash_table(t_count,s[i])>0:
                self.update_hash_table(curr_dict,s[i],1)
            
            s_sum.append(curr_dict)
       
        # check edge case where s does not have all chars of t
        last_prefix_sum= s_sum[len(s)-1]
        for i in range(52):
            if last_prefix_sum[i]<t_count[i]:return ""
        
        
        
        # 3 move the sliding window of size len(t_count) accross and check conditions
        sliding_window_size=len(index_with_nonzero_elems_in_t_count)
       
        
                
        win_condition=sliding_window_size
        
        res=s
        # sliding_window[start_index:end_index]=s[start_index,end_index)
        for start_index in range(0,len(s)):
            for end_index in range(start_index+sliding_window_size,len(s)+1):
                
                # get occurences of each key in t_count
              
                curr_streak=0 # if win_condition==len(t_count.keys)
                too_small=False

                for i in index_with_nonzero_elems_in_t_count:
                    
                    if start_index==0:
                        occurrences_for_this_char=s_sum[end_index-1][i]
                        
                    else:#start_index>=1:
                        occurrences_for_this_char=s_sum[end_index-1][i]-s_sum[start_index-1][i]
                    if occurrences_for_this_char<t_count[i]:
                        too_small=True
                        break
                    elif occurrences_for_this_char>=t_count[i]:
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
    input1 = "aa"
    input2 = "aa"
    excepted = "aa"
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

    input1 = "ADOBECODEBANC"
    input2 = "ABC"
    excepted = "BANC"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

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



    input1 = "a"
    input2 = "a"
    excepted = "a"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

