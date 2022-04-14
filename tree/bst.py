from tree.node import Node

class BST:
    def __init__(self):
        """Creates empty Binary Search Tree."""
        self.nil = Node(None)
        self.root = self.nil
        self.nil.height = -1

    def insert(self, x):
        x.left = x.right = self.nil
        if self.root == self.nil:
            self.root = x
            x.parent = self.nil
        else:
            node = self.root
            while node != self.nil:
                prev = node
                if x.key < node.key:
                    node = node.left
                else:
                    node = node.right

            x.parent = prev
            if x.key < prev.key:
                prev.left = x
            else:
                prev.right = x

        self.fix_height(x)

        return x

    def search(self, key):
        """Find and return the Node with key. Returns None if not found."""
        node = self.root
        while node != self.nil:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self, min_node=None):
        """Returns the Node with the minimum key."""
        if min_node is None:
            min_node = self.root
        if min_node == self.nil:
            return
        while min_node.left != self.nil:
            min_node = min_node.left
        return min_node

    def maximum(self, max_node=None):
        """Returns the Node with the maximum key."""
        if max_node is None:
            max_node = self.root
        if max_node == self.nil:
            return
        while max_node.right != self.nil:
            max_node = max_node.right
        return max_node

    def successor(self, x):
        """Find the immediately-following Node after Node x."""
        if x.right != self.nil:
            return self.minimum(x.right)
        else:
            p = x.parent
            while p != self.nil:
                if x == p.left:
                    return p
                else:
                    x = p
                    p = p.parent
            return None

    def delete(self, x):
        """Deletes Node x from the tree."""
        if self.root == self.nil:
            return
        if x.left != self.nil and x.right != self.nil:
            min_right = self.minimum(x.right)
            x.key, min_right.key = min_right.key, x.key
            x = min_right
        if x.right == self.nil and x.left == self.nil:
            y = self.nil
        elif x.right == self.nil:
            y = x.left
        elif x.left == self.nil:
            y = x.right
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent
        x.parent = x.left = x.right = None
        self.fix_height(y.parent)
        return x

    def rotate_left(self, x):
        p = x.parent
        y = x.right
        z = y.left

        y.left = x
        y.parent = p
        z.parent = x
        x.parent = y
        x.right = z
        if x == self.root:
            self.root = y
        else:
            if p.right == x:
                p.right = y
            else:
                p.left = y

        self.fix_height(x)

    def rotate_right(self, x):
        p = x.parent
        y = x.left
        z = y.right

        y.right = x
        y.parent = p
        z.parent = x
        x.parent = y
        x.left = z
        if x == self.root:
            self.root = y
        else:
            if p.right == x:
                p.right = y
            else:
                p.left = y

        self.fix_height(x)

    def fix_height(self, x):
        """Corrects the height of Node x (after insertion or deletion)."""
        node = x
        
        if node.left == self.nil and node.right == self.nil:
            node.height = 0
        else:
            node.height = max(node.left.height, node.right.height) + 1
        node = node.parent

        while node != self.nil and node.height != (mx := max(node.left.height, node.right.height) + 1):
            node.height = mx
            node = node.parent
        return x.height

    def print_tree(self, x=None, depth=0):
        """Prints the BST sideways."""
        if x is None:
            x = self.root
        if x != self.nil:
            self.print_tree(x.right, depth + 1)
            print("  " * depth + str(x.key))
            self.print_tree(x.left, depth + 1)

    def print_vert_tree(self):
        height = self.root.height
        width = 2 ** height
        q = list()
        q.append(self.root)

        for h in range(height):
            st = ""
            for _ in range(2 ** h):
                node = q.pop(0)
                if node == self.nil:
                    q.append(self.nil)
                    q.append(self.nil)
                    st += " " * (2 ** (height - h))
                else:
                    q.append(node.left)
                    q.append(node.right)
                    st += f"{node.key:^{2**(height-h)}}"
            print(st)
            
    def level_order_list(self):
        lvl_lst = []
        q = []
        q.append(self.root)
        while q:
            node = q.pop(0)
            if node == self.nil:
                continue
            lvl_lst.append(node.key)
            q.append(node.left)
            q.append(node.right)
        return lvl_lst
    
    def preorder_list(self, node=None, ans=None):
        """Modifies and returns ans. Starting at node, keys are appended to ans, with preorder traversal."""
        if ans is None:
            ans = []
        if node is None:
            node = self.root
        if node == self.nil:
            return ans
        ans.append(node.key)
        self.preorder_list(node.left, ans)
        return self.preorder_list(node.right, ans)

    def inorder_list(self, node=None, ans=None):
        """Modifies and returns ans. Starting at node, keys are appended to ans, with inorder traversal."""
        if ans is None:
            ans = []
        if node is None:
            node = self.root
        if node == self.nil:
            return ans
        self.inorder_list(node.left, ans)
        ans.append(node.key)
        self.inorder_list(node.right, ans)
        return ans

    def postorder_list(self, node=None, ans=None):
        """Modifies and returns ans. Starting at node, keys are appended to ans, with postorder traversal."""
        if ans is None:
            ans = []
        if node is None:
            node = self.root
        if node == self.nil:
            return ans
        self.postorder_list(node.left, ans)
        self.postorder_list(node.right, ans)
        ans.append(node.key)
        return ans


def main():
    tree = BST()
    for n in range(10):
        tree.insert(Node(n))
    tree.print_tree()
    print(tree.inorder_list())

if __name__ == "__main__":
    main()
