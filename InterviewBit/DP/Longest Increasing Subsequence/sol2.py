class Solution:
    def longest_sub(self,arr):
        if not arr:
            return 0
        length_array=len(arr)
        memo=[1]*length_array
        result_pointer=[]
        for i in range(0,length_array):
            result_pointer.append(i)
        for j in range(1,length_array):
            for i in range(j):
                if (arr[j]>=arr[i]):
                    if memo[i]>=memo[j]:
                        memo[j]=memo[i]+1
                        result_pointer[j]=i
        print (result_pointer)
        print (memo)
        current_arg_max=memo.index(max(memo))
        result=[]
        result.append(arr[current_arg_max])
        _max_=max(memo) # get the length of sequence to be added to result.
        for i in range(_max_-1):  # first element is already added in result above
            current_arg_max=result_pointer[current_arg_max]
            result.append(arr[current_arg_max])
        result.reverse()
        print (result)
input=[10,22,9,33,21,50,41,60]
sol_obj=Solution()
sol_obj.longest_sub(input)
