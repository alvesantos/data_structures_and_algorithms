from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if self.val is None:
            return None

        if val < self.val:
            if self.left:
                removed_node = self.left.delete(val)
                self.left = removed_node
            return self

        if val > self.val:
            if self.right:
                removed_node = self.right.delete(val)
                self.right = removed_node
            return self

        if val == self.val:
            if self.right is None:
                return self.left

            if self.left is None:
                return self.right

            min_size_right = self.right.get_min()

            self.val = min_size_right

            self.right = self.right.delete(min_size_right)

            return self

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

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val
