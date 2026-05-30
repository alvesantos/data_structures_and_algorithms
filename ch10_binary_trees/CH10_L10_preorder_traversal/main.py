from typing import Any


class BSTNode:
    def preorder(self, visited: list[Any]) -> list[Any]:
        if self.val is not None:
            visited.append(self.val)

        if self.left is not None:
            self.left.preorder(visited)

        if self.right is not None:
            self.right.preorder(visited)

        return visited

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
