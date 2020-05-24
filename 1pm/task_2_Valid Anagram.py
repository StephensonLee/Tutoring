# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false

s = "rat"
t = "car"
t=list(t)

for i in s:
    if i in t:
        t.remove(i)
    else:
        print("False")
        break
else:
    if len(t)==0:
        print("True")
    else:
        print("False")