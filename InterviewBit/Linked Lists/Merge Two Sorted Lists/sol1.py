class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=ListNode(data)
        new_node.next=self.head
        self.head=new_node
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self,left_head,right_head):
        left_pointer=left_head
        right_pointer=right_head
        head_merge_LL=ListNode(0) #dummy
        iter_merged=head_merge_LL
        while (left_pointer or right_pointer):
            if right_pointer is None:
                iter_merged.next=left_pointer
                iter_merged=iter_merged.next
                left_pointer=left_pointer.next
            elif left_pointer is None:
                iter_merged.next=right_pointer
                iter_merged=iter_merged.next
                right_pointer=right_pointer.next
            elif right_pointer.val<left_pointer.val:
                iter_merged.next=right_pointer
                iter_merged=iter_merged.next
                right_pointer=right_pointer.next
            else:
                iter_merged.next=left_pointer
                iter_merged=iter_merged.next
                left_pointer=left_pointer.next
        return head_merge_LL.next
def print_LL(head):
    current_node=head
    while (current_node is not None):
        print (current_node.val,end=' ')
        current_node=current_node.next
LL2=SLL()
LL2.push(13)
LL2.push(11)
LL2.push(10)
LL2.push(7)
LL3=SLL()
LL3.push(15)
LL3.push(12)
LL3.push(9)
LL3.push(6)
obj=Solution()
_head_=obj.mergeTwoLists(LL2.head,LL3.head)
print_LL(_head_)
