class Solution:
    def maxProfit(self,input):
        if len(input)==0:
            return 0
        max_profit=0
        buy=input[0] #buy on day zero
        for i in range(1,len(input)):
            if input[i]>=buy:
                profit=input[i]-buy
                max_profit=max(max_profit,profit)
            else:
                buy=input[i]
        return (max_profit)
sol_obj=Solution()
A=[3,4,40,1,20,50]
#A=[7,6,4,3,1]
print (sol_obj.maxProfit(A))

'''
Runtime: 40 ms, faster than 83.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 85.83% of Python3 online submissions for Best Time to Buy and Sell Stock.

Shorter version-
    def maxProfit(self,input):
        if len(input)==0:
            return 0
        max_profit=0
        buy=input[0] #buy on day zero
        for i in range(1,len(input)):
            buy=min(buy,input[i])
            if input[i]
            max_profit=max(max_profit,input[i]-buy)
        return (max_profit)
'''
