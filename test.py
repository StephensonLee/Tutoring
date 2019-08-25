# words =input()
n=4
sol=[1,2,3,4]
ans=["."*i + "Q" + "."*(n-i-1) for i in sol]
print ([i+1 for i in sol])
print(ans)
