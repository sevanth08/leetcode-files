"""
in this question we are given an array where i need to return if the array is good or not 
we need to check the arr and find the max[num] and see if the arr is in tht number's base ?
base[3] = [1,2,4,2]
base[2] = [1,3,4]

"""
s = list(map(int,input("enter the nums with space; ").split()))
x = max(s)
count = 0
count1 = 0
for num in s:
    if num == x:
        count+=1
    elif num!=x:
        count1 +=1

if len(s) != x+1 and (count !=2) :
    print(False)
else:
    good  = True
    for i in range(1,x):
        if s.count(i)!=1:
            good =False
            break
    print(good)
