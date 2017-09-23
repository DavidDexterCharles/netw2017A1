from gcd import gcd

def modulo(a, b, c):
    x=0
    y=a%c
    while b>0:
        if b%2 == 1:
            x = (x+y)%c
        y = (y*2)%c
        b/=2
    return x%c

def isPrime(p, iterations):
    
    if  p==1:
         return false