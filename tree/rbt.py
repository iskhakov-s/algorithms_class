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
