'''
O(n) time and O(n) space solution. More intuitive.
'''
def max_sum_1D(input):
    dp=[0]*(len(input)+1)
    dp[0]=0 # base case.
    dp[1]=input[0]
    for i in range(2,len(input)+1):
        dp[i]=max(dp[i-2]+input[i-1],dp[i-1])
    print (dp[-1])

input=[4,1,1,4,2,1]
max_sum_1D(input)
