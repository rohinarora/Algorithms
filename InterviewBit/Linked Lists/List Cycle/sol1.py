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
        s = set()  # hash
        temp_node=self.head
        while (temp_node):
            if (temp_node in s):
                return 1
            s.add(temp_node)  # we are pusing the objects into set. Objects are distinct, even if their "val" attribute is same
            temp_node=temp_node.next
        return 0

LL_obj = SLL()
LL_obj.push(20)
LL_obj.push(4)
LL_obj.push(15)
LL_obj.push(10)
LL_obj.print_LL()
print ("no cycles- ",LL_obj.detect())
#print (LL_obj.head.next.next.next.val)
LL_obj.head.next.next.next.next=LL_obj.head # create cycle
# don't use LL_obj.print_LL() with cycle. Infinite loop. Find a better way to print LL with cycles?
print ("cycle found- ",LL_obj.detect())
