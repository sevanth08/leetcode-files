"""
dynamic programming:
climbing a stairs inn 1 and 2 steps
"""
  
#approach 1
import math

total_ways = 0
num = int(input("enter the input: "))
for twos in range(num//2+1):    #
    ones = num -(2*twos)
    total_slots = twos + ones
    ways = math.factorial(total_slots)//(math.factorial(twos)*math.factorial(total_slots-twos))
    total_ways+=ways
print(total_ways)