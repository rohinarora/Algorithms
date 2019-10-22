'''
// If this is first column of current row 'i'
If j == 0
   // Then copy last entry of previous row
   // Note that i'th row has i entries
   Bell(i, j) = Bell(i-1, i-1)

// If this is not first column of current row
Else
   // Then this element is sum of previous element
   // in current row and the element just above the
   // previous element
   Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)
Example-
1
1 2
2 3 5
5 7 10 15
15 20 27 37 52

Bell(i,i) in i'th row gives bell number for that row (if i=n)
'''
def bellNumber(n):
    bell = [[0]*(n) for j in range(n)]
    bell[0][0] = 1 # fill first row
    print (bell)
    for i in range(1, n): # fill row wise 2nd row onwards
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    print (bell)
    return bell[n-1][n-1]

print (bellNumber(5))
