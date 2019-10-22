from binarytree import tree, bst, heap
my_bst = bst(height=3, is_perfect=True)
print(my_bst)

def in_order_traversal(x):
    if (x is not None):
        in_order_traversal(x.left)
        print (x.value, end=" ")
        in_order_traversal(x.right)
def in_order_traversal_stack(x): # x is root of the subtree
  if x==None:
    return
  stack=[]
  while(True):
    if (x!=None):
      stack.append(x)
      x=x.left
    else:
      if len(stack)==0:
        break # will reach here iff x is null and stack is empty. thats the termination condition
      else:
        x=stack.pop()
        print (x.value,end=" ")
        x=x.right
def pre_order_traversal(x):
    if (x is not None):
        print (x.value, end=" ")
        pre_order_traversal(x.left)
        pre_order_traversal(x.right)
def pre_order_traversal_stack(x): # x is root of the subtree
  if x==None:
    return
  stack=[]
  while(True):
    if (x!=None):
      # the moment you visit a node, print it
      print (x.value,end=" ")
      stack.append(x)
      x=x.left
    else:
      if len(stack)==0:
        break # will reach here iff x is null and stack is empty. thats the termination condition
      else:
        x=stack.pop()
        x=x.right
def post_order_traversal(x):
    if (x is not None):
        post_order_traversal(x.left)
        post_order_traversal(x.right)
        print (x.value, end=" ")
def post_order_traversal_stack(x): # x is root of the subtree
  if x==None:
    return
  stack=[]
  while(True):
    if (x!=None):
      stack.append(x)
      x=x.left
    else:
      if len(stack)==0:
        break # will reach here iff x is null and stack is empty. thats the termination condition
      elif stack[-1].right is not None:
          stack.append(stack[-1])
      else:
        x=stack.pop()
        print (x.value,end=" ")
        x=x.right
print ('in_order_traversal prints bst in sorted order')

print ('\n in_order_traversal: ')
in_order_traversal(my_bst)

print ('\n\n in_order_traversal_stack: ')
in_order_traversal_stack(my_bst)

print ('\n\n pre_order_traversal: ')
pre_order_traversal(my_bst)

print ('\n\n pre_order_traversal_stack: ')
pre_order_traversal_stack(my_bst)

print ('\n\n post_order_traversal: ')
post_order_traversal(my_bst)

print ('\n\n post_order_traversal_stack: ')
post_order_traversal_stack(my_bst)
