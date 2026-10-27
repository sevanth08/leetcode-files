"""
this question was, suggested by my friend Vishal an absurd question
you are given an list and another list called dictionary so you've asked to return the extra letter's count in the list 

ex:
input: s = 'sayhelloworld' dictionary = ['hello','world']
output = 3 beacause in the dictionary say was not there """

#approach 1
"""text = 'sayhelloworld'
dict = ["hello","world"]
res = []
for i in range(0,len(dict)):
    if dict[i] in text:
        start = text.find(dict[i])
        end = len(dict[i])+start
        str = text[:start]+text[end:]
        res.append(str)
common = set(res[0])
count = 0
for word in res[1:]:
    common = common & set(word)
for m in common:
    for i in range (len(res)):
        if m not in res[i]:
            pass
        count+=1
print(count)
"""
#approach 2
s = input("enter the text: ")
dictionary = input("enter the words: ").split()
words = set(dictionary)
n = len(s)
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i]=dp[i-1]+1
    for j in range(i):
        if s[j:i] in words:
            dp[i] = min(dp[i],dp[j])
print(dp[n]) 
print(words)