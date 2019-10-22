## takes extra space. naive solution. 
    def rotate(self,A):
        res=[[0]*len(A) for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][len(A)-i-1]=A[i][j]
        return res
