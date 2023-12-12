class Solution:

    def longestPalindrome_TLE(self, s: str) -> str:
        dp=dict()#dp[i,j]=true if si...sj is palindrome
        n=len(s)
   

        #set base case of len 1 and 2
        for i in range(n):
            dp[i,i]=True
            
            if i>n-2:continue
            if s[i]==s[i+1]:
                dp[i,i+1]=True
               
            else:
                dp[i,i+1]=False
        for j_offset in range(2,n):
            for i in range(0,n-j_offset):
                if dp[i+1,(i+j_offset)-1]:
                    if s[i]==s[i+j_offset]:
                        dp[i,i+j_offset]=True
                        
                    else:
                        dp[i,i+j_offset]=False
                else:
                    dp[i,i+j_offset]=False
        res=''
        for key in dp:
            if dp[key]:
                if key[1]-key[0]+1>len(res):
                    res=s[key[0]:key[1]+1]
                
        return res
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        n=len(s)
   

        #set base case of len 1 and 2
        for i in range(n):
            dp[i][i]=True
            
            if i>n-2:continue
            if s[i]==s[i+1]:
                dp[i][i+1]=True
               
            else:
                dp[i][i+1]=False
        for j_offset in range(2,n):
            for i in range(0,n-j_offset):
                if dp[i+1][(i+j_offset)-1]:
                    if s[i]==s[i+j_offset]:
                        dp[i][i+j_offset]=True
                        
                    else:
                        dp[i][i+j_offset]=False
                else:
                    dp[i][i+j_offset]=False
        res=''
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    if j-i+1>len(res):
                        res=s[i:j+1]
                
        return res
    def longestPalindrome_manacher(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1#keep track of the maximum length of the palindrome.
        Max_Str=s[0]#maximum substring.
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]#save the plinedrome radius
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:#update center and right bound
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:#update res
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str
if __name__ == "__main__":
    s=Solution()
    a="babad"#bab
    print(s.longestPalindrome(a))
    a="cbbd"#bb
    print(s.longestPalindrome(a))
    a='bb'#bb
    print(s.longestPalindrome(a))
    a="abcba"#"abcba"
    print(s.longestPalindrome(a))
    a="eabcb"#bcb
    print(s.longestPalindrome(a))
    a="mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj"
    #"vkkv"
    print(s.longestPalindrome(a))
    a="ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
    
    print(s.longestPalindrome_manacher(a))
    