from utils.test_driver import test_driver


class Solution:

    def longestPalindrome_TLE(self, s: str) -> str:
        dp = dict()  # dp[i,j]=true if si...sj is palindrome
        n = len(s)

        # set base case of len 1 and 2
        for i in range(n):
            dp[i, i] = True

            if i > n-2:
                continue
            if s[i] == s[i+1]:
                dp[i, i+1] = True

            else:
                dp[i, i+1] = False
        for j_offset in range(2, n):
            for i in range(0, n-j_offset):
                if dp[i+1, (i+j_offset)-1]:
                    if s[i] == s[i+j_offset]:
                        dp[i, i+j_offset] = True

                    else:
                        dp[i, i+j_offset] = False
                else:
                    dp[i, i+j_offset] = False
        res = ''
        for key in dp:
            if dp[key]:
                if key[1]-key[0]+1 > len(res):
                    res = s[key[0]:key[1]+1]

        return res

    # n^2
    def longestPalindrome_dp_n_square(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        n = len(s)

        # set base case of len 1 and 2
        for i in range(n):
            dp[i][i] = True

            if i > n-2:
                continue
            if s[i] == s[i+1]:
                dp[i][i+1] = True

            else:
                dp[i][i+1] = False
        for j_offset in range(2, n):
            for i in range(0, n-j_offset):
                if dp[i+1][(i+j_offset)-1]:
                    if s[i] == s[i+j_offset]:
                        dp[i][i+j_offset] = True

                    else:
                        dp[i][i+j_offset] = False
                else:
                    dp[i][i+j_offset] = False
        res = ''
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    if j-i+1 > len(res):
                        res = s[i:j+1]

        return res

    # manacher
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # base case
        if n <= 1:
            return s
        s = "#"+"#".join(s)+"#"

        # dp[i]=the diameter of the palinedrome string centered at i. Initially set to 1, since avery char is a plindrome
        dp = [1 for _ in s]
        max_right_center = -1
        # this is quite important. this represents the center of "the palinedrome 
        # that achieves the rightmost bound"
        max_right = -1# the rightmost bound of palinedrome substr
        n = len(s)
        # iterate thru every center in s
        for center in range(n):  # i is the curr center of the s

            # if it is possible to copy the palinedrom diameters from the mirrored index
            if max_right_center-(center-max_right_center) >= 0:
                dp[center] = min(# if center + copied diamter exceeds right bound, 
                    # we can only increae the diameter to touch the right bound. 
                    # The reason is that we cannot be sure that substrings centered 
                    # at 'center' with  diameter that exceeds right bound is palinedrome
                    dp[max_right_center-(center-max_right_center)], max_right-center)

            # expand the substring centered at 'center', starting with diameter=dp[center]
            while center-dp[center] >= 0 and center+dp[center] < n and s[center-dp[center]] == s[center+dp[center]]:
                dp[center] += 1

            # update max_right and max_right_center
            if center+dp[center] > max_right:
                max_right = min(center+dp[center], n)
                max_right_center = center

        # extract res
        max_dp = -1
        max_dp_index = -1
        for i, v in enumerate(dp):
            if max_dp < v:
                max_dp = v
                max_dp_index = i

        res=s[max_dp_index-max_dp+1:max_dp_index+max_dp]
        res=res.replace("#",'')
        return res


if __name__ == "__main__":
    s = Solution()

    tests = [
        ["abac", "aba"],
        ["babad", "bab"],
        
        ["cbbd", "bb"],
        
        ['bb', "bb"],
        
        ["abcba", "abcba"],
        
        ["eabcb", "bcb"],
        
        ["mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj",
        "vkkv"],
        
        ["ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi",
        "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"]
    ]
    for input, res in tests:
        test_driver(s.longestPalindrome, input, expected=res)
