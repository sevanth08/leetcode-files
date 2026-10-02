nums = list(map(int,input('enter the numbers with spaces; ').split()))
left = 0
total= sum(nums)
i = 0 
found = False
while i<len(nums):

    right = total-left -nums[i] 
    
    if left == right :
        print(f"pivot index at index:  '{i}' ")
        found = True
    left += nums[i]
    i+=1
    
if not found:
    print(-1)


