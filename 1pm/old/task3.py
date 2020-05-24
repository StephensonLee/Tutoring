# Say you have an array for which the i-th element is the price of 1pm given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


def maxProfit(k, prices) -> int:
    n = len(prices)
    if n<=1: return 0
    if k>n/2:
        res=0
        for i in range(1,n):
            res+=max(0,prices[i]-prices[i-1])
        return res
    dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(1,k+1):
            if i==0:
                dp[i][j][0]=0
                dp[i][j][1]=-prices[i]
                continue
            dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
            dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
    # return dp
    return dp[n-1][k][0]

prices=[3,2,6,5,0,4]
k = 2
dp=maxProfit(k,prices)
print(dp)
for i in range(len(prices)):
    print(dp[i])

