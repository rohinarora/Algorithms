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
    def deleteDuplicates(self, A):
        dummy=ListNode(0)
        dummy.next=A
        A=dummy
        one=A
        two=A.next
        three=A.next.next
        while (one and two and three):
            if (two.val==three.val):
                while((two and three and two.val==three.val) or (two and three and three.next and three.val==three.next.val)):
                    two=two.next
                    three=three.next
                one.next=three
                two=one.next
                if one.next:
                    three=one.next.next
            else:
                one=one.next
                two=two.next
                three=three.next
        return A.next
LL2=SLL()
LL2.push(15)
LL2.push(10)
LL2.push(10)
LL2.push(10)
LL2.push(10)
LL2.push(9)
LL2.push(7)
LL2.push(7)
LL2.push(7)
LL2.push(2)
LL2.push(2)
LL2.push(2)
LL2.push(1)
LL2.push(1)
print_LL(LL2.head)
obj=Solution()
_head_=obj.deleteDuplicates(LL2.head)
print_LL(_head_)
