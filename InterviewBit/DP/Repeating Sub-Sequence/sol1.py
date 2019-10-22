class Solution:
    def isPalindrome(self,temp,low,high):
        while (low<=high):
            if temp[low]!=temp[high]:
                return False
            low=low+1
            high=high-1
        return True
    def anytwo(self,input):
        # create a counter for each char in input
        dict_string={}
        for i in input:
            dict_string[i]=0
        for i in input:
            dict_string[i]=dict_string[i]+1
            if dict_string[i]>=3:
                return 1
        temp=""
        for i in input:
            if dict_string[i]>=2:
                temp=temp+i
        #print (temp)
        out= (self.isPalindrome(temp,0,len(temp)-1))
        #print ("palindrome output", out)
        if out:
            return 0
        else:
            return 1
sol_obj=Solution()
input="ABCABD"
input="ABBB"
input="AAB"
input="AABBC"
out=sol_obj.anytwo(input)
print (out)
