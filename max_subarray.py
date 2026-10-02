nums= list(map(int,input("enter no.s with spaces: ").split()))
curr_sum =0
max_sum =nums[0]
i =0
while i<len(nums):
    curr_sum = max(curr_sum + nums[i],nums[i])
    if curr_sum>=max_sum:
        max_sum=curr_sum
    if curr_sum<nums[i]:
        curr_sum = 0
    i+=1
print(max_sum)
