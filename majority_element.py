"""
this problems seems very easy; compared to tht is_subsequence 
we are given a list of elements we need to return the maximum times repeated number
input = [1,2,3,2,2,5,4,2,5]
output = 2

"""
nums = list(map(int,input("enter the number's with spaces; ").split()))
seen = {}
res=[]
for x in nums:
    seen[x] = seen.get(x,0)+1
for n in (seen.values()):
    res.append(n)
    n = max(res)
for key , value in seen.items():
    if value == n:
        keys = key
        break
print(keys)