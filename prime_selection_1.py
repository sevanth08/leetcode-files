"""
this is sworm problem statement
you are given two numbers 's' and 't'  
so bascically we need to get all the possible prime numbers below 's' 
and also return the maximized sum of number of prime numbers below 't' 

s = 15         #{2,3,7,11,13}
t = 15         # 2+3+7 = 12 
output = [2,3,5,7]
"""

n = int(input("enter N :"))
s = int(input("enter S :"))
res = []
res1 = []
res2 = []
total = 0
is_prime = [True]*(n+1)
is_prime[0] = is_prime[1] = False
for i in range(2,n+1):
    if is_prime:
        for j in range(i*i,n+1,i):
            is_prime[j] = False
for num in range(2,n+1):
    if is_prime[num]:
        if total + num > s:
            break
        else:
            res2.append(num)
            total+=num
print(res2)

" Sieve of Eratosthenes "