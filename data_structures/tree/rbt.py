from bst import BST
from node import Node

class RBNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.is_black = True
    
    def __str__(self):
        color = 'black' if self.is_black else 'red'
        return super.__str__() + f'; color={color}'


class RBTree(BST):
    def __init__(self):
        """Creates empty Binary Search Tree."""
        self.nil = RBNode(None)
        self.root = self.nil
        self.nil.height = -1
        
    def insert(self, x):
        """Inserts x into the red-black tree and rebalances."""
        ins = super().insert(x)
        x.is_black = False
        
        while not x.parent.is_black:
            # This while loop will take care of the repeating case 1.
            p = x.parent
            g = p.parent
            if not g.left.is_black and not g.right.is_black:
                # g's children (which are p and u) are red = case 1
                g.left.is_black = True
                g.right.is_black = True
                g.is_black = False
                x = g

            elif g.left == p:
                # p is left child, u is right child
                u = g.right
                if p.right == x:
                    # p is left child, x is right child = case 2
                    # ROTATE, then REASSIGN x to convert to case 3
                    self.rotate_left(p)
                    x, p = p, x
                    
                # p is left child, x is left child = case 3
                # ROTATE, then RECOLOR
                self.rotate_right(g)
                x.is_black = False
                g.is_black = False
                p.is_black = True
            else:
                # p is right child, u is left child
                u = g.left
                if p.left == x:
                    # p is right child, x is left child = case 2
                    # ROTATE, then REASSIGN x to convert to case 3
                    self.rotate_right(p)
                    x, p = p, x
                    
                # p is right child, x is right child = case 3
                # ROTATE, then RECOLOR
                self.rotate_left(g)
                x.is_black = False
                g.is_black = False
                p.is_black = True
                
        # This fixes the root color invariant.
        self.root.is_black = True
        return ins

    def delete(self, x):
        """Deletes node x and rebalances."""
        if self.root == self.nil:
            return
        if x.left != self.nil and x.right != self.nil:
            min_right = self.minimum(x.right)
            x.key, min_right.key = min_right.key, x.key
            x = min_right
        if x.right == self.nil and x.left == self.nil:
            y = self.nil
        elif x.right == self.nil:
            #x.left exists
            y = x.left
        elif x.left == self.nil:
            #x.right exists
            y = x.right
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent
        self.fix_height(y.parent)
        x.parent = x.left = x.right = None
        if x.is_black:
            self.delete_recolor(y)        
        return x

    def delete_recolor(self, x):
        while x != self.root and not x.is_black:
            if x == x.parent.left:
                # x is left, s is right
                # WRITE s
                s = x.parent.right
                if not s.is_black:
                    # case 1: convert to case 2/3/4
                    # two RECOLORs, one ROTATION, REASSIGN s
                    x.parent.is_black = False
                    s.is_black = True
                    self.rotate_left(x.parent)    
                
                if s.left.is_black and s.right.is_black:
                    # case 2: start over with the parent as x
                    # one RECOLOR, REASSIGN x
                    s.is_black = False
                    x = x.parent

                else:
                    if s.right.is_black:
                        # case 3: convert to case 4
                        # two RECOLORs, one ROTATION, REASSIGN s
                        s.left.is_black = False
                        s.is_black = True
                        self.rotate_right(s)
                        
                        
                    # case 4: fix this and finish
                    # three RECOLORs, one ROTATION, LEAVE loop
                    s.is_black = x.parent.is_black
                    x.parent.is_black = False
                    s.right.is_black = False
                    self.rotate_left(x.parent)
                    
            else:
                # x is right, s is left
                # WRITE s
                s = x.parent.left
                if not s.is_black:
                    # case 1: convert to case 2/3/4
                    # two RECOLORs, one ROTATION, REASSIGN s
                    x.parent.is_black = False
                    s.is_black = True
                    self.rotate_right(x.parent)    
                
                if s.left.is_black and s.right.is_black:
                    # case 2: start over with the parent as x
                    # one RECOLOR, REASSIGN x
                    s.is_black = False
                    x = x.parent

                else:
                    if s.left.is_black:
                        # case 3: convert to case 4
                        # two RECOLORs, one ROTATION, REASSIGN s
                        s.right.is_black = False
                        s.is_black = True
                        self.rotate_left(s)
                        
                        
                    # case 4: fix this and finish
                    # three RECOLORs, one ROTATION, LEAVE loop
                    s.is_black = x.parent.is_black
                    x.parent.is_black = False
                    s.left.is_black = False
                    self.rotate_right(x.parent)
        x.is_black = True
