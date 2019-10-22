class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self,num_rows):
        out=[]
        for i in range(num_rows):
            inner=[]
            for j in range(i+1):
                if (j==0) or (j==i):
                    inner.append(1)
                else:
                    inner.append(int(out[i-1][j]+out[i-1][j-1]))
            out.append(inner)
        return out
