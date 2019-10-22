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
        temp_node=Node(None)
        current_node=self.head
        while (current_node):
            if current_node.next==temp_node:
                return 1
            next_node=current_node.next
            current_node.next=temp_node
            current_node=next_node
        return 0

LL_obj = SLL()
LL_obj.push(20)
LL_obj.push(4)
LL_obj.push(15)
LL_obj.push(10)
LL_obj.print_LL()
print ("no cycles- ",LL_obj.detect())
# above line destroyed LL. Create the LL again
LL_obj = SLL()
LL_obj.push(20)
LL_obj.push(4)
LL_obj.push(15)
LL_obj.push(10)
LL_obj.print_LL()
#print (LL_obj.head.next.next.next.val)
LL_obj.head.next.next.next.next=LL_obj.head # create cycle
# don't use LL_obj.print_LL() with cycle. Infinite loop
print ("cycle found- ",LL_obj.detect())
