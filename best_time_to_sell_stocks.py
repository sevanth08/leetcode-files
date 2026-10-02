list=list(map(int,input("Enter the numbers with spaces: ").split()))
minval=list[0]
for i in list:
    if i < minval:
        minval = i
index = (list.index(minval))


maxval = list[index]
for j in list[index::]:
    if maxval < j:
        maxval = j

res = maxval-minval


if res ==0:
    if len(list) == 1:
        list.append(1)
    
    list.pop(index)
    
    minval =list[0]
    
    for i in list:
        if i<minval:
            minval = i

    maxval = list[list.index(minval)]
    for i in list[list.index(minval)::]:
        if maxval < i:
            maxval =i

            
print(maxval-minval)
    

    
    