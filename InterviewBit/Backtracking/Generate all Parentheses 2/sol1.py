class Solution:
    # @param A : integer
    # @return a list of strings
    def __init__(self):
        self.result=[]
    def generateParenthesisHelper(self,soFar,num):
        if soFar.count("(")==num:
            num_close=soFar.count(")")
            to_be_closed=num-num_close
            for i in range(to_be_closed):
                soFar=soFar+")"
            #print (soFar)
            self.result.append(soFar)
            return
        if soFar.count("(")==soFar.count(")"):
            self.generateParenthesisHelper(soFar+"(",num)
        else:
            self.generateParenthesisHelper(soFar+"(",num)
            self.generateParenthesisHelper(soFar+")",num)
    def generateParenthesis(self, num):
        self.generateParenthesisHelper("",num)
        return self.result
num=3
sol_obj=Solution()
out=sol_obj.generateParenthesis(num)
print (out)
