"""
valid anagram , i.e., you are given two words we need to check if the word is valid anagram 


input ={ t:'nagaram' 
        s:'anagram'}
        
output = true 

"""
t = input("enter the 1_string; ")
s = input("enter the 2_string; ")
seen_1 ={}
seen_2 ={}
for num in t:
    seen_1[num] = seen_1.get(num,0)+1
for num in s:
    seen_2[num] = seen_2.get(num,0)+1
if seen_1.items() == seen_2.items():
    print(True)
else:
    print(False)
