# Trees

Trees are a widely used data structure that simulate a hierarchical... well.. tree structure. That said, they're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

Trees are kind of like linked lists in the sense that the root node simply holds references to its child nodes, which in turn hold references to their children, but Tree's nodes can have multiple children instead of just one. A generic tree structure has the following rules:

- Each node has a value and may have a list of "children"
- Children can only have a single "parent"

## Linked List

```md
node -> node -> node
```

## Tree

Drawn from left to right in this case:

```md
         > node
      > node
   > node
> node
         > node
      > node
         > node
      > node
   > node
      > node
```

# Binary Trees

Trees aren't  particularly useful data structures unless they're ordered in some way. One of the most common types of ordered tree is a Binary Search Tree or `BST`. A `BST` has some additional constrains:

1. Instead of an unbounded list of children, each node has at most 2 children
2. The left child's value must be less than its parent's value
3. The right child's value must be greater than its parent's value
4. No two nodes is the `BST` can have the same value

By ordering the tree like this, we can traverse the tree to find the node we want much faster.

# Insert Nodes

The building blocks of a BST are Nodes. In our implementation, we will only use a single class, the `BSTNode` class. Any `BSTNode` is technically also a full Binary Search Tree, with itself as the root node (it's not aware of any potential parents). Most of the methods that traverse the tree will do so recursively... have fun!

## Our LockedIn `BSTNode`

Throughout this chapter we'll be building a binary search tree to power LockedIn's custom database. LockedIn's management doesn't trust so called "open-source"... so here we are. One of the primary freatures of databases is the ability to look up records by a single key, and binary search trees are the most common way to implement these fast lookups.

Each node in our BST will represent a LockedIn user. A `BSTNode` has three properties:

- `value`: The value of the node, a `User` object in our case (see `user.py`). You'll notice that `User`s have a name and an ID. Comparison operators are already implemented for you on the class, so you should be able to compare `User` objects with `==`, `<` and `>` directly. The ID is the value that we'll use to determine the order of the nodes in the tree. 
- `left`: The left child of the node, another `BSTNode` or `None`
- `right`: The right child of the node, another `BSTNode` or `None`

## Assignment

Complete the `insert` method of the `BSTNode` class. It takes a `User` object as input and adds it to a new node if the value doesn't already exist in the tree.

1. If the node doesn't have a vlue yet, store the given value and return
2. If the node's value is equal to the given value, just return, no duplicates allowed
3. If the given value is less than the node's value and the node doesn't have a `left` child, create a new `left` child node with the given value and return
4. If the given value is less than the node's value and the node does have a `left` child, recursively call `insert` off of that left child with the given value and return.
5. Since we already checked if the given value is equal to or less than the node, the value must be greater than the node. Handle wheather or not the node already has a `right` child.

### Tip

I'd highly recommend using pencil/paper or some kind of drawing tool to visualize the tree as you go through the assignments in this chapter.

[Go to code]()