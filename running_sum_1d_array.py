"""   
This is my 6th programme in Leetcode 
Problem statement ; you are given a list , so in the output the current output is the sum of the previous numbers in the list including the index we have now
ex.  input : [1,2,4,6]
     ouput : [1,3,7,13]  --->[1 , 1+2 , 1+2+4 , 1+2+4+6 ]

    for i in range (len(num))
        current = total + current
        total.append(everytime*)
        return 'res_final'    

"""
list = list(map(int,input("Enter the numbers with Spaces: ").split()))
total = 0
res_final =[]
for i in range(len(list)):
    current = list[i]
    total+=current
    res_final.append(total)
print(res_final)
