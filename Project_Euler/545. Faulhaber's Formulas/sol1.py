from fractions import Fraction
def fact(n):
    if (n==0) or (n==1):
        return 1
    output=1
    for j in range(1,n+1):
        output=output*j
    return output


def bern(m):
    output=0
    for k in range(0,m+1):
        for v in range(0,k+1):
            sum=Fraction((((-1)**v)*fact(k)*((v+1)**m)),(fact(v)*fact(k-v)*(k+1)))
            output=output+sum
    return output

for i in range(305,310):
    x=bern(i)
    if (x.denominator==20010):
        print (i)
