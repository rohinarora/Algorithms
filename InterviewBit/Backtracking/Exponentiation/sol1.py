import time
def pow(x,n): # O(n)
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)
def pow_fast(x,n): # O(log n)
    if n==0:
        return 1
    elif n%2==0:
        y=pow(x,n/2)
        return y*y
    else:
        return x*pow(x,n-1)
start = time.time()
print (pow(2,100))
end = time.time()
print (end - start)
start = time.time()
print (pow_fast(2,100))
end = time.time()
print (end - start)
