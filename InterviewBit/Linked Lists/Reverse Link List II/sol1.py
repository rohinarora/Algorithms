class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class SLL:
    def __init__(self):
        self.head=None
    def print_LL(self,head):
        current_node=head
        while (current_node is not None):
            print (current_node.val,end=' ')
            current_node=current_node.next
    def push(self,data):
        new_node=ListNode(data)
        new_node.next=self.head
        self.head=new_node
class Solution:
    def print_LL(self,head):
        current_node=head
        while (current_node is not None):
            print (current_node.val,end=' ')
            current_node=current_node.next
        print ("\n")
    def reverseBetween(self, A, B, C):
        if B==C:
            return A
        current=A
        prev=None
        for i in range(B-1):
            prev=current
            current=current.next
        #print (prev.val)
        save1=prev
        save2=current
        #print ("current ",current.val)
        #print (current.next.val)
        next=None
        for i in range(C-B):
            next=current.next
            current.next=prev
            prev=current
            current=next
        next=current.next # node 5
        save2.next=next # 2 points to 5
        if save1 is None:
            A=current
        else:
            save1.next=current # 1 points to 4
        current.next=prev # 4 points to 3
        #print ("first ",A.val)
        #print ("second ",A.next.val)
        #print ("third ",A.next.next.val)
        #print ("forth ",A.next.next.next.val)
        #print ("fifth ",A.next.next.next.next.val)
        #print ("last ",A.next.next.next.next.next)
        return A

def print_LL(head):
    current_node=head
    while (current_node is not None):
        print (current_node.val,end=' ')
        current_node=current_node.next
LL1 = SLL()
LL1.push(5)
LL1.push(4)
LL1.push(3)
LL1.push(2)
LL1.push(1)
print_LL(LL1.head)
print ("\n")
#print ("\n",LL1.head.val)
obj=Solution()
m=4
n=4
LL1.head=obj.reverseBetween(LL1.head,m,n)
print_LL(LL1.head)
#print (LL1.head.next.next.next.next.next.val)
