# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # '*' match empty string
    return dp[-1][-1]

s="aa"
p="a"

print(isMatch(s,p))