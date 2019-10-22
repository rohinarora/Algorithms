'''
O(n) time and O(1) space solution
'''
def max_sum_1D(input):
    exclusive=0  # max sum upto i excluding element i
    inclusive=input[0] # max sum upto i including element i
    for i in range(1,len(input)):
        temp=inclusive
        inclusive=max(exclusive+input[i],inclusive)
        exclusive=temp
    print (inclusive)

input=[4,1,1,4,2,1]
max_sum_1D(input)
