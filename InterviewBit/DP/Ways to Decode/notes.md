If input coded string is ""; output 1 (decoded message was "")
If input coded string is "01"; output 0. 0 isn't coded for any letter

Suffix problem

Example-
Ways2Decode(<string>) gives total ways to decode <string>

Ways2Decode(12345)=Decode(1)+Ways2Decode(2345)  (consider 1st character)
                    +
                   Decode(12)+Ways2Decode(345)  (consider 1st and 2nd character)

                   If in either of recursions above, first string can't be decoded, then terminate that branch of tree. It won't contribute to sum. There would be 2 such cases when first string can't be decoded-
                   1. You are considering 1st character and it is 0.
                   2. You are considering 1st and 2nd character and the number is > 26 or 1st character =0

Ways2Decode(278)= Decode(2)+Ways2Decode(78)
                  # Decode(27) not possible. Hence that branch doesn't contribute anything

Ways2Decode(011)=0      

sol1.py
Runtime: 24 ms, faster than 73.64% of Python online submissions for Decode Ways.
Memory Usage: 12.7 MB, less than 11.01% of Python online submissions for Decode Ways.

sol1 and sol2 are similar. sol1 feels more intuitive
sol3- bottom up O(n) time
sol4- bottom up O(1) time

ToDo-
Decode Ways II
see online solutions
see IB solution
see leetcode solution
