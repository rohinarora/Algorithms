#!/usr/local/bin/python3
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def print_LL(self):
        tmp_node=self.head
        if tmp_node is None:
            print ('empty LL')
        while (tmp_node is not None):
            print (tmp_node.val,end = " " )
            tmp_node=tmp_node.next
        print ("\n")
    def insert_start(self,data): # works even if there is no node in LL.
        tmp_node=Node(data)
        tmp_node.next=self.head.next
        self.head.next=tmp_node
    def insert_end(self,data):  # does it work with empty LL/corner cases
        tmp_node=Node(data)
        iter_node=self.head
        while (iter_node.next is not None):
            iter_node=iter_node.next
        iter_node.next=tmp_node

    def insert_inbetween(self,middle_node,new_data): # does it work with empty LL/corner cases
        if middle_node is None:
            print ('Middle node is absent')
            return
        tmp_node=Node(new_data)
        tmp_node.next=middle_node.next
        middle_node.next=tmp_node
    def remove_node(self,key):   # does it work with empty LL/corner cases
        current_node=self.head
        while current_node is not None:
            if current_node.val==key:
                prev_node.next=current_node.next
                current_node=None
                return
            prev_node=current_node
            current_node=current_node.next
        if current_node is None:
            print ("key not found")
            return
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
LL_obj=SLL()
LL_obj.head=Node(1) # first node
n2=Node(2) # second node
LL_obj.head.next=n2 #link first and second node
n3=Node(3)
n2.next=n3
n4=Node(4)
n3.next=n4
LL_obj.print_LL()

print ('blank LL example-')
LL_obj_empty=SLL()
LL_obj_empty.print_LL()
LL_obj.print_LL()
LL_obj.head=LL_obj.reverseList(LL_obj.head)
LL_obj.print_LL()
