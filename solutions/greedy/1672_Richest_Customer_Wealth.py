from cmath import inf


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max=-inf
        for row in accounts:
            sum=0
            for col in row:
                sum+=col
            if sum>max:
                max=sum
        return max

if __name__ == "__main__":
    accounts = [[1,2,3],[3,2,1]]
    s=Solution()

    print(s.maximumWealth(accounts=accounts))