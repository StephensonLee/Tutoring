def climbStairs(n: int) -> int:
    if n ==1:
        return 1
    elif n==2:
        return 2
    result= climbStairs(n - 1) + climbStairs(n - 2)
    return result

print (climbStairs(5))