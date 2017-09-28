'''
Name: David Charles
ID: 811000385
'''

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

# a=81
# b=57
# print gcd(a,b)