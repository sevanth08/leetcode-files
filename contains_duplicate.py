"""
the problem statement statess that if i was given a number then i must need to, return True if its duplicate 
or else you will have to return False

input = [1,2,3,4,5,1]

output = True
why because 1 appeared more than once

"""
list  = list(map(int,input("enter the no.s in spaces; ").split()))
seen={}
for letters in list:
    seen[letters] = seen.get(letters, 0)+1
print(seen
      )
for j in seen.values():
    if j>1:
        print(True)
        break
else:
    print(False)

