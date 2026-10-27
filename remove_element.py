"""
this problem states that, i need to returnt the len of the list as k after removing the occourances of the given val
 input = [1,2,1,5,2,]
 output = [1,1,5,_,_]
 we should return k  = 3  also orders of numbers can be changed
 
"""
nums= list(map(int,input("enter wkdb; ").split()))
val = int(input("enter the value; "))
k = 0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]  = nums[i]
        k+=1
print(k)
print(nums)