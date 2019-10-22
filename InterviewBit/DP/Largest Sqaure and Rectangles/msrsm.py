import sys
import math
def solve(row,col,M):
    matrix_max=-math.inf
    for L in range(col):
        L_R_sum=[0]*row
        for R in range(L,col):
            for j in range(row):
                L_R_sum[j]=L_R_sum[j]+M[j][R]
            # apply kadane on L_R_sum
            local_max=L_R_sum[0]
            global_max=L_R_sum[0]
            for j in range(1,row):
                local_max=max(L_R_sum[j],local_max+L_R_sum[j])
                global_max=max(global_max,local_max)
            matrix_max=max(matrix_max,global_max)
    print (matrix_max)
row = 4
col = 5
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

solve(row,col,M)
testcases=int(input())
for testcase in range(testcases):
    rows_cols=input()
    rows_cols= rows_cols.split()
    row=int(rows_cols[0])
    col=int(rows_cols[1])
    M_temp=input()
    M_temp=M_temp.split()
    M=[[0]*col for i in range (row)]
    counter=0
    for i in range(row):
        for j in range(col):
            M[i][j]=int(M_temp[counter])
            counter=counter+1
    solve(row,col,M)
