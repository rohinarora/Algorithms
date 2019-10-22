class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, k):
        zeros=[]
        for i in range(k+1):
            zeros.append(0)
        out=[zeros,zeros]
        for i in range(k+1):
            for j in range(i+1):
                if ((j==0) or (j==i)):
                    out[1][j]=1
                else:
                    out[1][j]=out[0][j]+out[0][j-1]
            out[0]=out[1].copy()
        return out[1]
