""" 
we are given an numsay we are said to be given an list which contains zeros and non-zeros so 
basically we have to move all the zeroes without disturbing the other non-zero no.s andd also no copying of the numsay!!

input = [1,0,2,5,6,0,4]

output = [1,2,5,6,4,0,0]

"""
nums = list(map(int,input("Enter the no.s with spaces in b/w: ").split()))
i =0
count=0
res =[]
while i< len(nums):
    if nums[i]==0:
        count+=1
    else:
        res.append(nums[i])
    i+=1

res.extend([0]*count)
nums[:] = res
print(nums)