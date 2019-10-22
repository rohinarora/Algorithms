class Solution:
    def subarraySum(self, nums, k):
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                sum_subarray=sum(nums[i:j+1])
                if sum_subarray==k:
                    count=count+1
        return count
sol_obj=Solution()
nums=[1,1,1]
k=2
out=sol_obj.subarraySum(nums,k)
print ("\n")
print (out)
