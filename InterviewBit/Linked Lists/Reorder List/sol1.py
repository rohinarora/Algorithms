class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
class SLL():
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
    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
    def print_LL(self,head):
        current_node=head
        while (current_node is not None):
            print (current_node.val,end=' ')
            current_node=current_node.next
    def reverseList(self, A):
        _prev=None
        _current=A
        _next=None
        while (_current is not None):
            _next=_current.next
            _current.next=_prev
            _prev=_current
            _current=_next
        return _prev
    def reorderList(self, A):
        length_LL=self.length_LL(A)
        if (length_LL)==1:
            return A
        # assuming length_LL is even
        mini_LL_length=int(length_LL/2)
        current=A
        for i in range(mini_LL_length-1):
            current=current.next
        new_list_head=current.next
        current.next=None
        #print ("\n")
        #print_LL(A)
        #print ("\n")
        #print_LL(new_list_head)
        save_val=new_list_head.val
        new_list_head=self.reverseList(new_list_head)
        #print ("\n")
        #print_LL(new_list_head)
        current_1=A
        current_2=new_list_head
        for i in range(mini_LL_length):
            save1=current_1.next
            save2=current_2.next
            current_1.next=current_2
            current_2.next=save1
            current_1=save1
            current_2=save2
        if (length_LL%2==1):
            current=A
            while (current.next is not None):
                current=current.next
            current.next=ListNode(save_val)
        return A
        #print ("\n")
        #print_LL(A)

LL1 = SLL()
LL1.push(8)
LL1.push(7)
LL1.push(6)
LL1.push(5)
LL1.push(4)
LL1.push(3)
LL1.push(2)
LL1.push(1)
print_LL(LL1.head)
obj=Solution()
obj.reorderList(LL1.head)
