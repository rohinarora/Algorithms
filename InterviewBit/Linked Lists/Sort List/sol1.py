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
    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
    def merge(self,left_head,right_head):
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
    def sortList(self, A):
        m=self.length_LL(A)
        if m==1:
            return A
        mid=m/2
        current=A
        for i in range(int(mid)-1):
            current=current.next
        LL2=current.next #6
        current.next=None # break LL A into 2 halves
        LL1=A
        sorted_left=  self.sortList(LL1)
        sorted_right=  self.sortList(LL2)
        return self.merge(sorted_left,sorted_right)
def merge(left_head,right_head):
    left_pointer=left_head
    right_pointer=right_head
    print ("\n")
    l1=print_LL(left_head)
    print ("\n")
    l2=print_LL(right_head)
    print ("\n")
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
LL1 = SLL()
LL1.push(5)
LL1.push(2)
LL1.push(3)
LL1.push(6)
LL1.push(10)
LL1.push(100)
LL1.push(20)
LL1.push(60)
#print_LL(LL1.head)
#print ("\n")
obj=Solution()
_head_=obj.sortList(LL1.head)
#print ("\n")
print_LL(_head_)
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
#print ("\n")
#print_LL(merge(LL2.head,LL3.head))
