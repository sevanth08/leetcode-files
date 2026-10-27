"""
the problem clearly says that we need to return the intersection of two lists  
i,e,. return the elements which is present in both of the list in common

input = [1,2,2,3,3,3]
        [5,,2,3,4,6,5]
        
output = [2,3]

why because 2 & 3 are the only common elements 

"""
res= []
seen_1 = {}
seen_2 = {}
nums_1 = list(map(int,input("enter the 1st list elements; ").split()))
nums_2 = list(map(int,input("enter the 2ndst list elements; ").split()))

for num in nums_1:
    seen_1[num] = seen_1.get(num,0)+1

for num in nums_2:
    seen_2[num] = seen_2.get(num,0)+1
    
for i in  seen_1.keys():
    if i in seen_2.keys():
        res.append(i)
print(res)
