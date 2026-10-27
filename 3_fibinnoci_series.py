"""
this question is a very different from others coz 
we are given an input number such tht we need to say oif this number can be expressed in terms of the fibinocci serie, like 

iput = 2
output = 0+1+1

input = 10
output = 2+3+5

"""
n = int(input("enter the number: "))
i = 0
a,b = 0, 1
res = [0]
while a+b<n:
    a,b = a+b,a
    res.append(a)
    i+=1
found = False
i = 0
while i<n:
    total = res[i]+res[i+1]+res[i+2]
    if total == n:
        print(True)
        found = True
        break
    elif total < n:
        i+=1
    elif total > n:
        print(False)
        found = True
    if found == True:
        break
if found == False:
    print(False)