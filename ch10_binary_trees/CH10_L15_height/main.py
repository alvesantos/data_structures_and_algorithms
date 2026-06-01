from typing import Any


class BSTNode:
    def height(self) -> int:
        left = 0
        right = 0
        
        if self.val is None:
            return 0
        
        if self.left is not None:
            result = self.left.height()
            left = result

        if self.right is not None:
            result = self.right.height()
            right = result

        return max(left, right) + 1

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
