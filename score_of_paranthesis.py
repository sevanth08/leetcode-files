"""
this question is quite confusing ,we are given a str tht contains
braces like this we need to add or multiply number of paranthesis based on how they are present 
()()   -->  AB = A+B 

(A)    -->  2*A = RESULT

"""
s = input("enter the string; ")
depth  = 0 
score  = 0 
for i in range(len(s)):
    if s[i] == "(":
        depth +=1

    elif s[i] == ")":
        if s[i-1] == "(":
            score += 2**(depth -1)
        depth -=1
print(score) 