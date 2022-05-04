class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.height: int = 0
    
    def __str__(self):
        return f'key={self.key}; left={self.left.key}; right={self.right.key}; parent={self.parent.key}; height={self.height}'
