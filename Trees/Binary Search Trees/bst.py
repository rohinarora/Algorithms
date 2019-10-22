class BST(object):
    """
    Simple BST
    Each tree contains some (maybe 0) BSTnode objects, representing nodes, and a pointer to the root.
    """
    def __init__(self):
        self.root = None

    def insert(self,t):
        '''
        Insert key in BST
        '''
        new_node=BSTnode(t)
        y=None
        x=self.root
        while (x is not None):
            y=x
            if new_node.key<x.key:
                x=x.left
            else:
                x=x.right
        new_node.parent=y
        if y==None:
            self.root=new_node
        elif new_node.key<y.key:
            y.left=new_node
        else:
            y.right=new_node
        return new_node
    # this return helps only if you use further bstsize.py
    # helps update all the parent nodes in augmented bst

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        x=self.root
        while (x is not None):
            if x.key==t:
                return x
            elif t<x.key:
                x=x.left
            else:
                x=x.right
        return None
    def delete_min(self): # kinda like extract min from heap
        """Delete the minimum key (and return the old node containing it)."""
        if self.root is None:
            print ("Nothing to delete. No BSTnode in tree")
            return None, None  # this return helps only if you use further bstsize.py
        else:
            x=self.root
            while (x.left is not None):
                x=x.left
            # x is the leftmost node
            if x.parent is not None:
                x.parent.left=x.right
            else: # The root was smallest.
                self.root=node.right
            if x.right is not None:
                x.right.parent = x.parent
            parent = x.parent
            x.disconnect()
            return x,parent # this return helps only if you use further bstsize.py
    def inorder_tree_walk(self,x):
        '''
        print BST in sorted order
        '''
        if (x is not None):
            self.inorder_tree_walk(x.left)
            print (x.key)
            self.inorder_tree_walk(x.right)

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])



class BSTnode(object):
    """
    Node of a BST.
    It has left, right child, parent, and a key value
    """
    def __init__(self, t):
        """Create a new leaf with key 'key'."""
        self.key = t
        self.disconnect()
    def disconnect(self):
        self.right=None
        self.left=None
        self.parent=None

def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print ('usage: {} <number-of-random-items | item item item ...>'.format(sys.argv[0]))
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    #print (tree)
    for item in items:
        tree.insert(item)
        #print (tree)
    print (tree)
    #tree.inorder_tree_walk(tree.root)

if __name__ == '__main__': test()
