class Solution:
    def maxProfit(self,input):
        if len(input)==0:
            return 0
        total_profit=0
        max_profit=0
        buy=input[0] #buy on day zero
        for i in range(1,len(input)):
            if input[i]>=input[i-1]:
                profit=input[i]-buy
                max_profit=max(max_profit,profit)
            else:
                total_profit=total_profit+max_profit
                buy=input[i]
                max_profit=0
        total_profit=total_profit+max_profit
        return (total_profit)
sol_obj=Solution()
A=[3,4,40,1,20,50]
#A=[7,6,4,3,1]
#A=[1,2,3,4,5]
#A=[7,1,5,3,6,4]
print (sol_obj.maxProfit(A))
'''
Runtime: 36 ms, faster than 91.74% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14 MB, less than 54.25% of Python3 online submissions for Best Time to Buy and Sell Stock II.

'''
