#Calculating GCD of two numbers using Euclid's alogorithm


def gcd(a,b):
    m,n=max(a,b),min(a,b)
    
    if m%n:
        return gcd(n,m%n)
    else:
        return n

a=int(input())
b=int(input())

print("GCD of",a,"and",b,"=",gcd(a,b))

'''

If d divides both m and n and n does not divide n, 
so, m = qn + r,
and m = ad , n = bd,

so,  ad = q(bd) + r 

So, m mod n must also be divisible by d.

So, the algo is

        if n divides m, return n
        else, return gcd(n,m mod n)

'''