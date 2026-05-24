class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return 
        
        if self.val == val:
            return

        if self.val > val and not self.left:
            self.left = BSTNode(val)
            return

        if self.val > val and self.left:
            self.left.insert(val)
            return

        if self.val < val and not self.right:
            self.right = BSTNode(val)
            return

        if self.val < val and self.right:
            self.right.insert(val)
            return