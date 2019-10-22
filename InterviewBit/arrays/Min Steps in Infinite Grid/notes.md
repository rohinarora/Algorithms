Submission:
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps=0
        if len(A)==1:
            return steps
        for i,point in enumerate(A):
            if ((i+1)==len(A)):
                break
            dist_x=abs(A[i]-A[i+1])
            dist_y=abs(B[i]-B[i+1])
            two_points=max(dist_x,dist_y)
            steps=steps+two_points
        return steps

Jupyter:
A=[0,0,3]
B=[0,4,5]
def coverPoints(A, B):
    steps=0
    if len(A)==1:
        return steps
    for i,point in enumerate(A):
        if ((i+1)==len(A)):
            break
        dist_x=abs(A[i]-A[i+1])
        dist_y=abs(B[i]-B[i+1])
        two_points=max(dist_x,dist_y)
        steps=steps+two_points
    return steps
