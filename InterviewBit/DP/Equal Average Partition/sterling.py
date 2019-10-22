'''
S(n, k) = k*S(n-1, k) + S(n-1, k-1)
S(n,0)=0
S(0,n)=0
S(0,0)=1 (base cases). 3rd base case not used in practice
https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values
'''
def countP(n, k):
    # Base cases
    if (n == 0 and k == 0):
        return 1
    elif (n == 0 or k == 0 or k > n):
        return 0
    elif (k == 1 or k == n):
        return 1

    # S(n+1, k) = k*S(n, k) + S(n, k-1)
    return (k * countP(n - 1, k) +
                countP(n - 1, k - 1))
n=1
k=1
print (countP(n, k))
