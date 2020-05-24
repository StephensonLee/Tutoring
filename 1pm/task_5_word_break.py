# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
#
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

# def dfs(s, wordDict, memo):
#     if s in memo:
#         return memo[s]
#     res = []
#     for i in range(1, len(s) + 1):
#         s1 = s[:i]
#         s2 = s[i:]
#         if s1 in wordDict:
#             res_s2 = dfs(s2, wordDict, memo)
#             for substr in res_s2:
#                 if substr == "":
#                     res.append(s1)
#                 else:
#                     res.append(s1 + " " + substr)
#     memo[s] = res
#     return res
#
#
# def wordBreak(s, wordDict):
#     # write your code here
#     memo = {}
#     memo[""] = [""]
#     return dfs(s, wordDict, memo)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
def sep(sentence,worddict):
    list=[]

    for i in worddict:
        if sentence[:len(i)]==i:
            if sentence[len(i):]=="":
                list.append(i)
            else:
                cur = sep(sentence[len(i):], worddict)
                for j in cur:
                    list.append(i+" "+j)
    return list

print(sep(s,wordDict))

