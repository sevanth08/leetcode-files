"""

max water in container 
formula = (right-left)*(min(height[left],right[height]))

input = [1,8,6,2,5,4,8,3,7]
output = 49
note: we have to return max area possible...
 
"""

height = list(map(int,input("enter the no.s with spaces; ").split()))

i = 0
j =len(height)-1
max_area = 0
found =False
while i<j:
   
    area = (j-i)*(min(height[i],height[j]))
    if area > max_area:
        max_area = area
    if height[i]<height[j]:
            i+=1
    else:
        j-=1

print(max_area) 