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
def print_LL(head):
    print ("\n")
    current_node=head
    while (current_node is not None):
        print (current_node.val,end=' ')
        current_node=current_node.next
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        m=self.length_LL(A)
        if m==1:
            return A
        iterations=int(m/2)
        dummy=ListNode(0)
        dummy.next=A
        A=dummy
        prev=dummy
        current=prev.next
        next=current.next
        for i in range(iterations):
            save_iter_current=next.next
            prev.next=next
            next.next=current
            current.next=save_iter_current
            prev=current
            current=save_iter_current
            if current:
                next=current.next
        return A.next
    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
LL2=SLL()

LL2.push(2)
LL2.push(1)
print_LL(LL2.head)
obj=Solution()
_head_=obj.swapPairs(LL2.head)
print_LL(_head_)
