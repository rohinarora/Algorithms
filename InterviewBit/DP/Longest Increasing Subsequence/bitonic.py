class Solution:
    def longestSubsequenceLength(self, A):
        if not A:
            return 0
        lis_memo=self.lis(A)
        lds_memo=self.lds(A)
        #print (lis_memo)
        #print (lds_memo)
        lbs_memo=[]
        for i in range(len(lis_memo)):
            lbs_memo.append(lis_memo[i]+lds_memo[i]-1)
        #print (lbs_memo)
        return max(lbs_memo)
    def lis(self, A): # equivalent to lis from left to right
        if not A:
            return 0
        length_array=len(A)
        memo=[1]*length_array
        for j in range(1,length_array):
            for i in range(j):
                if A[j]>A[i]:
                    memo[j]=max(memo[j],memo[i]+1)
        return (memo)
    def lds(self, A): # equivalent to lis from right to left
        if not A:
            return 0
        length_array=len(A)
        memo=[1]*length_array
        for j in range(length_array-2,-1,-1):
            for i in range(j+1,length_array):
                if A[j]>A[i]:
                    memo[j]=max(memo[j],memo[i]+1)
        return (memo)
sol1=Solution()
input=[80,60,30,40,20,10]

print (sol1.longestSubsequenceLength(input))
