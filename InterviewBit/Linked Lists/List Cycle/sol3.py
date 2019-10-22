# hashing
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def print_LL(self):
        current_node=self.head
        while (current_node is not None):
            print (current_node.val,end=' ')
            current_node=current_node.next
        print ("\n")
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def detect(self):
        if not self.head:
            return None
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                break
        if slow_p!=fast_p:
            return None
        slow_p=self.head
        while (slow_p!=fast_p):
            slow_p=slow_p.next
            fast_p=fast_p.next
        return slow_p

LL_obj = SLL()
LL_obj.push(20)
LL_obj.push(4)
LL_obj.push(15)
LL_obj.push(10)
LL_obj.print_LL()
print ("cycle found- ",LL_obj.detect())
#print (LL_obj.head.next.next.next.val)
LL_obj.head.next.next.next.next=LL_obj.head # create cycle
# don't use LL_obj.print_LL() with cycle. Infinite loop
print ("cycle found- ",LL_obj.detect().val)
