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
    # @return the head node in the linked list
    def insertionSortList(self, A):
        save_head=A
        current=A
        while (current is not None):
            next=current.next
            insert_iter=save_head  # needs update. For when smallest element replaces save_head
            prev_iter=None
            while (insert_iter!=current):
                if insert_iter.val>current.val:
                    prev.next=next
                    current.next=insert_iter
                    if prev_iter is not None:
                        prev_iter.next=current
                    else:
                        save_head=current
                    break
                prev_iter=insert_iter
                insert_iter=insert_iter.next
            if (current.next==next):
                prev=current  # else prev remains the same
            current=next
        return save_head


LL1 = SLL()
LL1.push(5)
LL1.push(2)
LL1.push(3)
LL1.push(6)
LL1.push(10)
print_LL(LL1.head)
obj=Solution()
_head_=obj.insertionSortList(LL1.head)
print ("\n")
print_LL(_head_)
