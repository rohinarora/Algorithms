def print_2D_list(_list_):
    for i in range(len(_list_)):
        for j in range(len(_list_[i])):
            print (_list_[i][j]),
        print ('\n')
class Solution:
    def minDistance(self,A,B):
        A=" "+A
        B=" "+B
        len_A=len(A)
        len_B=len(B)
        ED=[ [0] * len_B for _ in range(len_A)]
        for i in range(len_A):
            ED[i][0]=i
        for i in range(len_B):
            ED[0][i]=i
        for i in range(1,len_A):
            for j in range(1,len_B):
                if A[i]==B[j]:
                    ED[i][j]=ED[i-1][j-1]
                else:
                    ED[i][j]=min(ED[i-1][j],ED[i][j-1],ED[i-1][j-1])+1
        return ED,ED[i][j]


A="Anshuman"
B="Antihuman"
sol_obj=Solution()
table,out=sol_obj.minDistance(A,B)
print(out)
print_2D_list(table)
