from utils.test_driver import test_driver


class Solution:

    def shortestPalindrome(self, s: str) -> str:
        original_s=str(s)
        # manacher to create dp table for palinedrome len
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

        # find the longest subtr that starts at index 0, and is palinedrome
        max_dp = -1
        max_dp_index = -1
        for i, v in enumerate(dp):
            if max_dp < v and i-v+1==0:
                max_dp = v
                max_dp_index = i
    
        res=s[max_dp_index-max_dp+1:max_dp_index+max_dp]
        res=res.replace("#",'')

        to_add=original_s[len(res):]
        return to_add[::-1]+original_s


if __name__ == "__main__":
    s = Solution()

    tests = [
            ["abb",'bbabb'],
            ["abcd","dcbabcd"],
            ["aacecaaa","aaacecaaa"],
        ]
    for input, res in tests:
        test_driver(s.shortestPalindrome, input, expected=res)
# idea:1.find the longest palinedrome substring in s that starts at 0
#      2.find to_add=s[len("longest palinedrome substring"):]
#      3.res=to_add[::-1]+"longest palinedrome substring"