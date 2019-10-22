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
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        m=self.length_LL(A)
        if m<B:
            return A
        iterations=int(m/B)
        dummy=ListNode(0)
        dummy.next=A
        A=dummy
        prev=dummy
        current=A.next
        save_current=current
        save_prev=prev
        for i in range(iterations): # in each iteration reverse B length of LL. updating start at end of each iteration
            for j in range(B):
                next=current.next
                current.next=prev
                prev=current
                current=next
            save_prev.next=prev
            save_current.next=next
            save_prev=save_current
            save_current=current
        return A.next

    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
LL2=SLL()
LL2.push(6)
LL2.push(9)
LL2.push(1)
LL2.push(11)
LL2.push(3)
LL2.push(13)
print_LL(LL2.head)
obj=Solution()
rotate=6
_head_=obj.reverseList(LL2.head,rotate)
print_LL(_head_)
