"""
we are given a list in which we need to return the index value of the numbers which make the sum upto the target number

input = [2,3,5,4,6,1]
target = 0

output = [1,4]

where 1 & 4 are the indexes of the numbers which add upto target 3+6 = 9 (target) 

"""
nums =list(map(int,input("enter the no's with spaces; ").split()))
target = int(input("enter the target; "))
j = -1
i = 0
while i <len(nums):
   num = target - nums[i]
   for num in nums:
    if num in nums:
        
        i+=1