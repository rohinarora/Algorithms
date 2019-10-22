import copy
class Solution:
    def solve(self, A):
        rows=len(A)
        if rows==0:
            return 0
        cols=len(A[0])
        if cols==0:
            return 0
        aux=copy.deepcopy(A)
        for j in range(cols):
            for i in range(1,rows):
                if aux[i][j]!=0:
                    aux[i][j]=aux[i-1][j]+1
        for i in range(rows):
            aux[i].sort(reverse=True)
        __max__=-1
        for i in range(cols):
            for j in range(rows):
                aux[j][i]=aux[j][i]*(i+1)
                __max__=max(__max__,aux[j][i])
        return (__max__)
input=[[0,1,0,1,0],[0, 1, 1, 1, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 1]]
sol_obj=Solution()
print (sol_obj.solve(input))
