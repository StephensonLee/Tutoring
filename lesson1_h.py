def solveNQueens(n):
    def dfs(queens,xy_sum,xy_diff):
        print(queens)
        # print(queens,xy_sum,xy_diff)
        q = len(queens)
        if q == n:
            ans.append(queens)
            return
        for i in range(n):
            if i not in queens and (i+q) not in xy_sum and (q-i) not in xy_diff:
                dfs(queens+[i],xy_sum+[i+q],xy_diff+[q-i])
    ans = []
    dfs([],[],[])
    print (ans)
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]

print(solveNQueens(4))