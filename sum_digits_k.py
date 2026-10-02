#this is my 5th programme in leetcode
"""     so bascially this problems says tht:
        input: 34
        k = 3
        ----/---= //  ,  %  
    1.   34 / 3 = 11  ,  1
    2.   11 / 3 = 3  ,  2
    3.   3 / 3 = 1  ,  0
        
        output = 0+2+1 = " 3  "
"""
n = int(input("enter the input: "))
k = int(input("enter the base: "))
remainder = []
for i in range(n): 
    rem = n%k 
    floor = n//k
    remainder.append(rem)
    n = floor
print(remainder)
total = 0
for i in range (len(remainder)):
    total += remainder[i]
print(total) 