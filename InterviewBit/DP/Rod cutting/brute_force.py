import math
class Solution:
    def cut_rod(self,P,n):
        if n==0:
            return 0
        else:
            q=-math.inf
            for i in range(0,n):
                optimal_val_at_i_cut=P[i]+self.cut_rod(P,n-i-1)
# Why cut_rod(P,n-i-1). Becuase-
# P[0] means cut at 1 inch. Python indexing starts from 0. Corresponding subproblem is cut_rod(P,n-1) which makes sense
# P[n-1] means no cut. Corresponding subproblem is cut_rot(P,n-(n-1)-1) or cut_rot(P,0); which makes sense
                if optimal_val_at_i_cut>q:
                    q=optimal_val_at_i_cut
        return q

sol_obj=Solution()
P=[1,5,8,9,10,17,17,20,24,30]
for i in range(1,len(P)+1):
    out=sol_obj.cut_rod(P,i)
    # prints Pg 362 CLRS. confirms code is correct
    print (out)
