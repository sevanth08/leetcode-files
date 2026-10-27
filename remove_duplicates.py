"""
we are given a list containing duplictaes , we need to return the original no. s without changing the original order and also making sure adding 
'_' in place eof the duplicates

input = [1,1,2]
output = [1,2,_]

input = [0,0,1,1,1,2,2,3,3,4]
output=[0,1,2,3,4,_,_,_,_,_]

"""
nums= list(map(int,input("enter the no's with spaces; ").split()))
k = 1
for i in range(1,len(nums)):
    if nums[i] != nums[k-1]:
        nums[k] = nums[i]
        k+=1
print(k)
