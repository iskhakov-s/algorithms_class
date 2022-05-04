from tree.bst import BST
from tree.node import Node

class AVL(BST):
    def bf(self, x):
        return x.left.height - x.right.height

    def insert(self, x):
        super().insert(x)
        ins = x
        while x != self.nil:
            if self.bf(x) == 2:
                if self.bf(x.left) == -1:
                    self.rotate_left(x.left)
                self.rotate_right(x)
                break
            elif self.bf(x) == -2:
                if self.bf(x.right) == 1:
                    self.rotate_right(x.right)
                self.rotate_left(x)
                break
            else:
                x = x.parent
        return ins

    def delete(self, x):
        ins = x
        super().delete(x)
        x = x.parent
        self.bf(self.root)
        while x != self.nil:
            if self.bf(x) == 2:
                if self.bf(x.left) == -1:
                    self.rotate_left(x.left)
                self.rotate_right(x)
                break
            elif self.bf(x) == -2:
                if self.bf(x.right) == 1:
                    self.rotate_right(x.right)
                self.rotate_left(x)
                break
            else:
                x = x.parent
        return ins
        

def main():
    tree = AVL()
    for n in range(10):
        tree.insert(Node(n))
    tree.print_tree()
    print(tree.inorder_list())

if __name__ == "__main__":
    main()
