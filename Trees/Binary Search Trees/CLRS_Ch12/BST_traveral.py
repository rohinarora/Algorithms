from binarytree import tree, bst, heap
my_bst = bst(height=3, is_perfect=True)
print(my_bst)

def in_order_traversal_recursive(current):
    if (current is not None):
        in_order_traversal_recursive(current.left)
        print (current.value, end=" ")
        in_order_traversal_recursive(current.right)

def in_order_traversal_stack(current): # current is root of the subtree
  if current==None:
    return
  stack=[]
  while(True):
    if (current!=None):
      stack.append(current)
      current=current.left
    else:
        if (stack):
            current=stack.pop()
            print (current.value,end=" ")
            current=current.right
        else: #Termination condition
            break # will reach here iff current is null and stack is empty.

def in_order_morris_traversal(current):
    '''
    in_order_morris_traversal
    O(n) time, O(1) space
    -> If we have left leaving tree, traversal will create temporarily
    "height of left subtree" extra pointers.
    But that doesn't contribute to extra space. All those nodes were initially
    pointing to None, and then they temporarily point to some node in upper tree.
    No new space needed
    Fun fact: print statement comes at 2 places here.
    Came only once via stack approach.
    '''
    while (current!=None):
        if (current.left==None):
            print (current.value,end=" ")
            current=current.right
        else:
            pred=current.left
            while ((pred.right!=None) and (pred.right!=current)):
                pred=pred.right
            if pred.right==None:
                pred.right=current
                current=current.left
            else:
                pred.right=None
                print (current.value,end=" ")
                current=current.right

def pre_order_traversal_recursive(current):
    if (current is not None):
        print (current.value, end=" ")
        pre_order_traversal_recursive(current.left)
        pre_order_traversal_recursive(current.right)

def pre_order_traversal_stack(current): # current is root of the subtree
  if current==None:
    return
  stack=[]
  while(True):
    if (current!=None):
      print (current.value,end=" ")
      stack.append(current)
      current=current.left
    else:
        if (stack):
            current=stack.pop()
            current=current.right
        else: #Termination condition
            break # will reach here iff current is null and stack is empty.

def pre_order_morris_traversal(current):
    while (current!=None):
        if (current.left==None):
            print (current.value,end=" ")
            current=current.right
        else:
            pred=current.left
            while ((pred.right!=None) and (pred.right!=current)):
                pred=pred.right
            if pred.right==None:
                print (current.value,end=" ")
                pred.right=current
                current=current.left
            else:
                pred.right=None
                current=current.right

def post_order_traversal_recursive(current):
    if (current is not None):
        post_order_traversal_recursive(current.left)
        post_order_traversal_recursive(current.right)
        print (current.value, end=" ")

def post_order_traversal_two_stack(current):
    stack1=[]
    stack2=[]
    stack1.append(current)
    while (stack1):
        stack2.append(stack1.pop())
        if stack2[-1].left:
            stack1.append(stack2[-1].left)
        if stack2[-1].right:
            stack1.append(stack2[-1].right)
    while(stack2):
        print (stack2[-1].value,end=" ")
        stack2.pop()


def post_order_traversal_one_stack(current):
    stack=[]
    while(True):
        if (current!=None):
            stack.append(current)
            current=current.left
        else:
            if (stack):
                temp=stack[-1].right
                if temp!=None:
                    current=temp
                else:
                    tmp=stack.pop()
                    print (tmp.value, end=" ")
                    while ((stack) and tmp==stack[-1].right):
                        tmp=stack.pop()
                        print (tmp.value,end =" ")

            else: # stack empty and current None
                break

print ('in_order_traversal prints bst in sorted order')

print ('\n in_order_traversal_recursive: ')
in_order_traversal_recursive(my_bst)

print ('\n\n in_order_traversal_stack: ')
in_order_traversal_stack(my_bst)

print ('\n\n in_order_morris_traversal: ')
in_order_morris_traversal(my_bst)

print ('\n\n pre_order_traversal_recursive: ')
pre_order_traversal_recursive(my_bst)

print ('\n\n pre_order_traversal_stack: ')
pre_order_traversal_stack(my_bst)

print ('\n\n pre_order_morris_traversal: ')
pre_order_morris_traversal(my_bst)

print ('\n\n post_order_traversal_recursive: ')
post_order_traversal_recursive(my_bst)

print ('\n\n post_order_traversal_two_stack: ')
post_order_traversal_two_stack(my_bst)

print ('\n\n post_order_traversal_one_stack: ')
post_order_traversal_one_stack(my_bst)
