"""
we need to check if there are any consecutive numbers in the list in o(n) time 

input = [0,3,1,6,2,3]
output = 4

why beacuse  0,1,2,3 are the consecutive numbers arranged at different indices.

"""
#approach 1
res = []
count = 1
current_count = 0
nums = [1,3,2,4,5,7,786]
nums_set = set(nums)
for curr in ((nums_set)):
    current_count = 1
    while curr+1 in nums_set:
        current_count+=1
        curr +=     1
    if current_count>count:
        count = current_count
print(count)