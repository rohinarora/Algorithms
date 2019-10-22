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
    def length_LL(self):
        current_node=self.head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        print (count)
class Solution:
    def print_LL(self,head):
        current_node=head
        while (current_node is not None):
            print (current_node.val,end=' ')
            current_node=current_node.next
        print ("\n")
    def length_LL(self,head):
        current_node=head
        count=0
        while (current_node is not None):
            count=count+1
            current_node=current_node.next
        return (count)
    def addTwoNumbers(self,A, B):
        length_1=self.length_LL(A)
        length_2=self.length_LL(B)
        pointer_1=A
        pointer_2=B
        carry=0
        result=None
        for i in range(max(length_1,length_2)):
            if pointer_1 is None:
                a=0
            else:
                a=pointer_1.val
            if pointer_2 is None:
                b=0
            else:
                b=pointer_2.val
            sum=a+b+carry
            res=sum%10
            carry=int(sum/10)
            new_node=Node(res)
            new_node.next=result
            result=new_node
            pointer_1=pointer_1.next
            pointer_2=pointer_2.next
        if carry==1:
            new_node=Node(1)
            new_node.next=result
            result=new_node
        #return result
        # reverse result
        _prev=None
        _current=result
        _next=None
        while (_current is not None):
            _next=_current.next
            _current.next=_prev
            _prev=_current
            _current=_next
        result= _prev
        return result
number1 = SLL()
number1.push(5)
number1.push(4)
number1.push(4)
number1.print_LL()
number2 = SLL()
number2.push(4)
number2.push(5)
number2.push(6)
number2.print_LL()
obj=Solution()
res=obj.addTwoNumbers(number1.head,number2.head)
obj.print_LL(res)
