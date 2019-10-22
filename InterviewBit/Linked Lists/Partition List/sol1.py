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
    current_node=head
    while (current_node is not None):
        print (current_node.val,end=' ')
        current_node=current_node.next
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        pass
        LL_small=ListNode(0) # initialize dummy node
        LL_big=ListNode(0) # initialize dummy node
        LL_small_head=LL_small # save head
        LL_big_head=LL_big # save head
        current=A # start iterating over LL A
        while (current is not None):
            if current.val <B:
                LL_small.next=current
                LL_small=LL_small.next
            else:
                LL_big.next=current
                LL_big=LL_big.next
            current=current.next
        LL_big.next=None
        LL_small.next=LL_big_head.next
        return LL_small_head.next

LL1 = SLL()
LL1.push(2)
LL1.push(5)
LL1.push(2)
LL1.push(3)
LL1.push(4)
LL1.push(1)
print_LL(LL1.head)
obj=Solution()
partition_int=3
_head_=obj.partition(LL1.head,partition_int)
print ("\n")
print_LL(_head_)
