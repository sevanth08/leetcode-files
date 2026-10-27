"""
this question is easy asf...
see wea re given a list of numbers of range  0,n so in tht range we neeed to return the no. tht is missing

input = [0,3,1]       ----     so actually we count from 1 
output = 2

"""
s = list(map(int,input("enter the no.'s with space; ").split()))
for i in range(0,len(s)+1):
    if i not in s:
        print(i)
        break
    