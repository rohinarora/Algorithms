'''
Runtime: 60 ms, faster than 88.46% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 14.8 MB, less than 60.63% of Python3 online submissions for Largest Rectangle in Histogram.
'''
class Solution:
    def largestRectangleArea(self, heights):
        stack=[]
        max_area=-1
        idx=0
        while (idx<len(heights)):
            if (len(stack)==0) or heights[idx]>=heights[stack[-1]]:
                stack.append(idx)
                idx=idx+1
            #elif heights[idx]<heights[stack[-1]]:
            else:
                top_idx=stack.pop()
                if len(stack)==0:
                    area=heights[top_idx]*(idx)
                    max_area=max(max_area,area)
                else:
                    area=heights[top_idx]*(idx-stack[-1]-1)
                    max_area=max(max_area,area)
        while (len(stack)!=0):
            top_idx=stack.pop()
            if len(stack)==0:
                area=heights[top_idx]*(idx)
                max_area=max(max_area,area)
            else:
                area=heights[top_idx]*(idx-stack[-1]-1)
                max_area=max(max_area,area)
        return max_area
        # pop everything remaining and repute area



sol_obj=Solution()
heights=[2,1,5,6,2,3]
out=sol_obj.largestRectangleArea(heights)
print (out)
