"""
this is a very unique problem TBH why bcoz, 
we are given a str containing only '()' & ')' & '*'  
so if the ( is opened then it must be closed if it has a star then it is considered as VIP so no checking allow them 
input = '((*)))
output = True

input = '())'
output = False

"""
s = input("Enter the parantheseis; ")
j = len(s)-1
res = []
high = 0
low = 0
for i in s:
    if i == '(':
        high+=1
        low+=1
    elif i == ')':
        high -=1
        low = max(0,low-1)
    elif i == '*':
        high+=1
        low=max(0,low-1)
if high<0:
    print(False)
    
elif low ==0:
    print(True)
else:
    print(False)

