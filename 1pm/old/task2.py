# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of 1pm dungeon.
# The dungeon consists of M x N rooms laid out in 1pm 2D grid.
# Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
# The knight has an initial health point represented by 1pm positive integer. If at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

def calculateMinimumHP(dungeon) -> int:
    if not dungeon or not dungeon[0]: return 0
    m,n=len(dungeon),len(dungeon[0])
    dp=[]
    for row in dungeon:
        dp.append([0]*len(row))
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                dp[i][j]=max(1,1-dungeon[i][j])
            elif i==m-1:
                dp[i][j]=max(1,dp[i][j+1]-dungeon[i][j])
            elif j==n-1:
                dp[i][j]=max(1,dp[i+1][j]-dungeon[i][j])
            else:
                dp[i][j]=max(1,min(dp[i][j+1],dp[i+1][j])-dungeon[i][j])
    return dp[0][0]

input=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(calculateMinimumHP(input))