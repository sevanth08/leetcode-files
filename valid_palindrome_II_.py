"""
this problem iss very unique one IDK why this isn't in hard or medium level 
we usual we are given a string to check palindrome but we need to check even after removing a letter from it 
if its still a palindrome

input = 'abca'
output = True    c can be deleted

input = 'abcd'
output = False

"""
i = 0

s = input("enter the string; ")
j = len(s)-1
i = 0 
res=[]
if s == s[::-1]:
    print(True)
while i<j :
    if s[i] != s[j]:
        a = s[i+1:j+1]
        b  = s[i:j]
        if a ==a[::-1] or b==b[::-1]: 
            print(True)
            break
        else:
            print(False)
            break
    i+=1
    j-=1
