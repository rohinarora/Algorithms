class Solution:
    def longest_sub(self,arr):
        if not arr:
            return 0
        length_array=len(arr)
        memo=[1]*length_array
        for j in range(1,length_array):
            for i in range(j):
                if (arr[j]>=arr[i]):
                    memo[j]=max(memo[j],memo[i]+1)
        print (memo)
        max_val=max(memo)
        result=[]
        for j in range(len(arr)-1,-1,-1):
            if max_val==memo[j]:
                result.append(arr[j])
                max_val=max_val-1
        result.reverse()
        print (result)
input=[10,22,9,33,21,50,41,60]
sol_obj=Solution()
sol_obj.longest_sub(input)
