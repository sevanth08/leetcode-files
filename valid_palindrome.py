"""A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward 
and backward. Alphanumeric characters include letters and numbers. 
        input = "A man, a plan, a canal: Panama"         input = "race a car"
        output = "True"                                  output = False

"""
import re
s= input("enter the input: ")
s = re.sub(r'[^a-zA-Z]','',s).lower()
if s == s[::-1]:
    print(True)
    print(s)
else:
    print(False)
    print(s)