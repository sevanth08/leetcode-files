"""
THIS IS  A PROBLEM WHERE I WILL HAVE TO CHEKC FOR XOR (A+B) OPERATION ON ADJACENT ELEMENTS IN THE LIST...

EX: input = [1,1,2,2,3,3,]
    output = 3
    
"""
count = 0
num = list(map(int,input("enter the num: ").split()))
for i in range(0,len(num)-1):
    j = i+1
    if num[j]==num[i]:
        count+=1
print(count)
