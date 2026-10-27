s = input("Enter the valid string: ")
count = 0
opened  = 0
closed = 0
for i in s:
    if i == ")":
        if opened>0:
            opened -=1
        else:
            count+=1
    elif i =="(":
        opened+=1
    
print(count + opened)

