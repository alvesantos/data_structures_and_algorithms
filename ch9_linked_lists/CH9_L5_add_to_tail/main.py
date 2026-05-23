from node import Node


class LinkedList:
    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return

        last_node_viewed = self.head

        for current_node in self:
            last_node_viewed = current_node

        last_node_viewed.set_next(node)

        

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
