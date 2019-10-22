'''
Given an array A;
dp[i]-> mcss ending at A[i]
For each index i; 2 choices
1. Do i start a new subarray starting at index i?
2. Do i extend the previous mcss created by A[:i-1]
also re create the solution
'''
class Solution:
    def maxSubArray(self, nums):
        if len(nums)==0:
            return 0
        max_current=nums[0]
        max_global=nums[0]
        for i in range(1,len(nums)):
            max_current=max(nums[i],max_current+nums[i])
            max_global=max(max_global,max_current)
        return (max_global)
sol_obj=Solution()
A=[-2,1,-3,4,-1,2,1,-5,4]
sol_obj.maxSubArray(A)

'''
Runtime: 36 ms, faster than 97.53% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.7 MB, less than 53.51% of Python3 online submissions for Maximum Subarray.
'''
