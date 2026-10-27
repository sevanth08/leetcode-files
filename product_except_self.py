"""
i think i have solved this typa question i dont remember exaclty but i have solved it, 
anyways we'll solve it again, and 

the problem statement say tht we ahve to return an list in which in evbvery element's

position we have to reutrn the product of the remaining elements in tht list 

input  = [1,5,4,9]
output = [180,36,45,20]

input = [1,2,3,4]
output = [24,12,8,6]

"""
nums = [2,4,3,5,8]
res = [1]*len(nums)
prefix = 1 
for i in range(len(nums)):
    res[i] = prefix
    prefix*=nums[i]
suffix = 1
for i in range(len(nums)-1,-1,-1):
    res[i] *= suffix
    suffix*=nums[i]
print(res)