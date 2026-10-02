""" # return the indexes of TwoSum problem in a list* 
        input = [2,3,1,5,6]
        target = 8
        output = [1,3] 1 and 3 are indexes

"""
def two_sum_2():
     = list(map(int,input("enter the numbers with spaces: ").split()))
    =numbers.sort()
    r= len(=numbers)-1
    l=0
    target =int(input("Enter the no. : "))
    while l<r :
        current_sum = =numbers[l]+=numbers[r] 
        if current_sum == target :
            print([l+1,r+1])  
            print(=numbers)
            return
        elif current_sum<target:
            l+=1
        else:
            r-=1
    print("no answers found")
two_sum_2() 