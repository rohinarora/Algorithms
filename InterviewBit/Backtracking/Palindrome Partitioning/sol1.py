class Solution:
    # @param A : string
    # @return a list of list of strings
    def __init__(self):
        self.result=[]
    def partitionHelp(self,soFar,input_string,current_pointer):
        if current_pointer==len(input_string):
            self.result.append(soFar[:])
            return
        for i in range(current_pointer,len(input_string)):
            snippet=input_string[current_pointer:i+1]
            if snippet==snippet[::-1]:  # if palindrome
                soFar.append(snippet)  # choose
                self.partitionHelp(soFar,input_string,i+1)
                soFar.pop()            # unchoose
    def partition(self, input_string):
        self.partitionHelp([],input_string,0)
        return (self.result)


input_string="aacc"
sol_obj=Solution()
out=sol_obj.partition(input_string)
print (out)
