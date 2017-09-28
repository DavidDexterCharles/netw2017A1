import random
import  sys #http://www.pythonforbeginners.com/system/python-sys-argv
from gcd import gcd

# def modulo(a, b, c):
#     x=0
#     y=a%c
#     while b>0:
#         if b%2 == 1:
#             x = (x+y)%c
#         y = (y*2)%c
#         b/=2
#     return x%c

def isPrime(p, iterations):
    if  p==1:
         return False
    for i in range(iterations):
        r = random.randint(2, p) -1 
        
       # if gcd(p,r) > 1:
       #     return False
        #if modulo(r,p-1,p) != 1:
        if  pow(r, p-1, p) != 1:
            return False
    return True


print isPrime(int(sys.argv[1]) ,int(sys.argv[2]))


#i=0
# try:
#     while isPrime(int(sys.argv[1]) ,int(sys.argv[2]))!= True:
#         i=i+1
# except:
#     print "Invalid Parameters"

# print str(i) +" iterations made"