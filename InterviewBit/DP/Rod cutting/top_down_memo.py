class Solution:
    def __init__(self):
        self.memo={}
    def cut_rod(self,P,n):
        if n in self.memo:
            return self.memo[n]
        if n==0:
            self.memo[n]=0
            return 0
        else:
            q=-1
            for i in range(0,n):
                optimal_val_at_i_cut=P[i]+self.cut_rod(P,n-i-1)
                # P[0] means cut at 1 inch. Python indexing starts from 0
                # P[n-1] means no cut. Hence cut_rot(P,n-(n-1)-1) or cut_rot(P,0)
                if optimal_val_at_i_cut>q:
                    q=optimal_val_at_i_cut
                    cut=i+1
        self.memo[n]=q
        return q,cut

sol_obj=Solution()
P=[1,5,8,9,10,17,17,20,24,30]
for i in range(1,len(P)+1):
    out,cut=sol_obj.cut_rod(P,i)
    # prints Pg 362 CLRS. confirms code is correct
    print (out,cut)
