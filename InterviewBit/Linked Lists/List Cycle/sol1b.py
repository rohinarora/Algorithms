# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self,head):
        s = set()  # hash
        temp_node=head
        while (temp_node):
            if (temp_node in s):
                return temp_node
            s.add(temp_node)
            temp_node=temp_node.next
        return None
