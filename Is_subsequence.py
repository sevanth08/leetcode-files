"""
this one really got me , we are given an str and 't' str we need to check if this t-str is in order in str
i.e.,  str = 'lkjhg'   t = 'ljg'             t = 'lgj'
                                                
    output = True                         output = False   
    
    because ljg exists in str in same order as it is in str 
"""
res = []
t = input("Enter the string; ")
s = input("Enter the sequence to enter; ")
res = []
start = 0
for i in s :
    for j in range(start,len(t)):
        if i == t[j]:
            res.append(j)
            start=j+1
            break
if sorted(res) == res and len(s) == len(res):
    print(True)
else:
    print(False)
