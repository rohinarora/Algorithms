class Solution:
    def path_calculate(self,i,j,path):
        if(i+1==j):
            return []
        k = path[i][j]
        if(k == 0):
            return []
        return [k] + self.path_calculate(i,k,path) + self.path_calculate(k,j,path)
    def rodCut(self, A, B):
        if(len(B)==0):
            return []
        if(len(B)==1):
            return B
        B = [0] + B + [A]
        n = len(B)
        cost = [[0 for i in range(len(B))] for j in range(len(B))]
        path = [[0 for i in range(len(B))] for j in range(len(B))]
        for l in range(2,len(cost)):
            for i in range(n-l):
                j = i + l
                mink = i+1
                min_val = cost[i][mink] + cost[mink][j]
                for k in range(i+1,j):
                    if min_val > cost[i][k] + cost[k][j]:
                        min_val = cost[i][k] + cost[k][j]
                        mink = k
                cost[i][j] = B[j] - B[i] + min_val
                path[i][j] = mink
        print (cost)
        ans_path = self.path_calculate(0,len(B)-1,path)
        ans = [B[i] for i in ans_path]
        return ans
A=[1,2,5]
ans=Solution().rodCut(6, A)
print (ans)
