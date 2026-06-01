from typing import Any


class BSTNode:
    def exists(self, val: Any) -> bool:
        if self.val == val:
            return True
        
        if self.val > val:
            if self.left is not None:
                return self.left.exists(val)
                
        if self.val < val:
            if self.right is not None:
                return self.right.exists(val)

        return False

        # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
