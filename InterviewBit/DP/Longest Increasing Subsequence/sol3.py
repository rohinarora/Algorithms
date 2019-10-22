'''
longest_subHelper(self,arr,i)- gives the length of LIS update ith index
'''
import math
class Solution:
    def longest_subHelper(self,arr,i):
        if i==0:
            return 1
        else:
            q=-math.inf
            for j in range(i-1,-1,-1):
                if arr[i]>arr[j]:
                    q=max(q,self.longest_subHelper(arr,j)+1)
        return q


    def longest_sub(self,arr):
        return self.longest_subHelper(arr,len(arr)-1)
input=[10,22,9,33,21,50,41,60]
sol_obj=Solution()
out=sol_obj.longest_sub(input)
print (out)
