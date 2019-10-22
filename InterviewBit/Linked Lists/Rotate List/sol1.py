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
    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
    def rotateRight(self, A, B):
        m= self.length_LL(A)
        rotate=B%m
        #print (rotate)
        current=A
        for i in range(m-rotate-1):
            current=current.next
        end=current
        start=end.next
        print (current.val)
        current=A
        while (current.next is not None):
            current=current.next
        old_end=current
        old_end.next=A
        A=start
        end.next=None
        return A
LL2=SLL()
LL2.push(5)
LL2.push(4)
LL2.push(3)
LL2.push(2)
LL2.push(1)
print_LL(LL2.head)
obj=Solution()
rotate=2
_head_=obj.rotateRight(LL2.head,rotate)
print_LL(_head_)
