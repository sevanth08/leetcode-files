"""
this question need not to be explained as , the title itself suggests us that we need to retun the longest common prefix..

inout = ["flight","flawless","flag"]
output = "fl" 

"""
words = input("enter the str list:").split()
i = 0
seen = {}
res = ""

shortest = min((len(word)) for word in words)
for i in range(shortest):
    ch = words[0][i]
    if all(word[i] == ch for word in words):
        res+=ch
    else:
        break
print(res)