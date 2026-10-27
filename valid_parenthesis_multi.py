"""
this problem is same as validf parenthesis , we are given a str which contains multo parenthesis 
"""
s = input("enter the parenthesis; ")
count1 = 0
count2 = 0
count3 = 0
for i in s:
    if i =='(':
        count1+=1
    elif i == ')':
        count1-=1
    if i =='[':
        count2+=1
    elif i == ']':
        count2-=1
    if i =='{':
        count3+=1
    elif i == '}':
        count3-=1
if count1==count2==count3 ==0:
    print(True)
else:
    print(False)