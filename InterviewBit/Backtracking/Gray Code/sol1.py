class Solution:
    # @param A : integer
    # @return a list of integers
    def __init__(self):
        self.result=[]
    def grayCodeHelper(self,soFar,Rest,depth):
        #print (soFar)
        if len(soFar)==depth:
            str_soFar= (''.join(str(x) for x in soFar))
            int_soFar= (int(str_soFar,2))
            self.result.append(int_soFar)
            return
        self.grayCodeHelper(soFar+[Rest[0]],[0,1],depth)
        self.grayCodeHelper(soFar+[Rest[1]],[1,0],depth)

    def grayCode(self, num):
        self.grayCodeHelper([],[0,1],num)
        return self.result

num=2
sol_obj=Solution()
out=sol_obj.grayCode(num)
print (out)
