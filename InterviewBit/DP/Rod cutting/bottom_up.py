import math
class Solution:
    def cut_rod(self,P,n):
        R=[0]*(n+1)
        S=[-1]*(n+1)
        R[0]=0
        S[0]=0
        for i in range(1,n+1):
            q=-math.inf
            for j in range(0,i):
                optimal_val_at_i_cut=P[j]+R[i-j-1]
                if optimal_val_at_i_cut>q:
                    q=optimal_val_at_i_cut
                    S[i]=j+1
            R[i]=q
        return R,S
sol_obj=Solution()
P=[1,5,8,9,10,17,17,20,24,30]
cost,cut=sol_obj.cut_rod(P,len(P))
print ("\n\n\nmax price is : ",cost)
print ("cut position is: ",cut)
