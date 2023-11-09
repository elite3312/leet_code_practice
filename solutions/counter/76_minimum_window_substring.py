from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get counts of chars in t
        t_counts = Counter(t)
        # create a counter for keeping track of chars in w
        w = Counter()
        # keep track of shortest answer found so far
        r = ''
        # keep track of which characters we have in the current window
        window = deque()
        for ch in s:
            # add current character to window
            window.append(ch)
            # increment count in window
            w[ch] += 1
            # check if predicate is satisfied (window contains all chars in t)
            if all(w[c] >= t_counts[c] for c in t_counts.keys()):
                # remove unnecessary (superfluous) chars
                while window and w[window[0]] > t_counts[window[0]]:
                    w[window.popleft()] -= 1
                # record this new answer only if it is shorter than a previous answer
                # (or if no previous answer exists)
                if r == '' or len(window) < len(r):
                    r = ''.join(window)
                # remove the last added char so we can keep looking for more substrings
                if window:
                    w[window.popleft()] -= 1
           
        return r
    def minWindow_tle(self, s: str, t: str) -> str:
        # we use prefix_sum sums
        if len(t) > len(s):
             return ''
        # 1. loop through t, and count occurences of unique characters in t
        t_count=[0]*52# upper case*26+lower case*26 
        for c in t:
            if 65<=ord(c)<=90:
                t_count[ord(c)-65]+=1
            else:
                t_count[ord(c)-71]+=1

        index_with_nonzero_elems_in_t_count=[]
        for i in range(52):
            if t_count[i]>0:
                index_with_nonzero_elems_in_t_count.append(i)
        
        # check edge case where len(t)==1:
        if len(t)==1:
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
            if 65<=ord(s[i])<=90:
                if t_count[ord(s[i])-65]>0:
                    curr_dict[ord(s[i])-65]+=1
            else:
                if t_count[ord(s[i])-71]>0:
                    curr_dict[ord(s[i])-71]+=1
            s_sum.append(curr_dict)
       
        # check edge case where s does not have all chars of t
        last_prefix_sum= s_sum[len(s)-1]
        for i in range(52):
            if last_prefix_sum[i]<t_count[i]:return ""
        
        
        
        # 3 move the window of size len(t_count) accross and check conditions
        window_size=len(t)
        win_condition=len(index_with_nonzero_elems_in_t_count)      
        
        res=s
        # window[start_index:end_index]=s[start_index,end_index)
        for start_index in range(0,len(s)):
            for end_index in range(start_index+window_size,len(s)+1):
                
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
                    if end_index-start_index == window_size:
                        return s[start_index:end_index]
                    
        return res
    
               


if __name__ == "__main__":

    s = Solution()
    input1 = "mspkqlcdmrwgrmcaytxilusinwgjvkdhfuuvfwarpxaglegjyftlblvqjezhqeovyisfgtxvqzdbdlmbthowumnfqomitbetlyzsrwpjvvkygycbfsyzgnfwbrhwunqilpadnrmkmzkvzowfhwgnjnmlftjbgzjtolwddlnrmymlmlsvhzltmzgtspvapetfqsjvfymrybelmxivwtokuueokbobhkgzerujqjcomgbadmxbhmociuquvhxereexvainlkcxsfxyrvzzjpbtjrqgynlrtpqrryedkiadqabhxcigslbdftkfhvxcmptdoagykjdajekgjsodgrgllqqulpwzfsdvsjtcszfddplojbrptyagqtaeiydnqgiksepmduqildxwfqmaqoghhilqiqfbxqlrucdzythlzgiexwepkmwuwjmeatfzjtqfxtewpohourutnajamhwiriotbwsnpismdxkunskhjedzeozsvvaofrhinzvcjoqpnbjavwjgcohjcgbadeokvytizomjeearhlrchdlkrstwbwwgamrxkkhkatvfavwhgqmqvzamrviutebutstfcbpcwmjwjigqyuittkhmfqhywkupcqvgrmkpbumkcuacokxhuevzwcatmwkqmhwfwjvxfjhhdkltuicpoxqlcsgqpshdafjwqevvpcesmpljzpyomqbqjjhabqddvozoswjhzobndowfdwvsnwiwhryihbmfqntkkculsxyyoxdrtyliwwgdnenvgbcypvkbzgmsemqujvlftzprvwwialfinjieetfgbtahhqbtlnagop"
    input2 = "zjlxtmibwxkfbraixbdx"
    excepted = "wtokuueokbobhkgzerujqjcomgbadmxbhmociuquvhxereexvainlkcxsf"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "baBBba"
    input2 = "aB"
    excepted = "aB"
    ans = s.minWindow(input1,input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ",ans)
    print('expected:', excepted)

    input1 = "aabaabaaab"
    input2 = "bb"
    excepted = "baab"
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

