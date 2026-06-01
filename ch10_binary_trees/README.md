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

# Delete

We also need a way to remove users from our BST if a user decides to delete their account.

## Assignment

Implement the recursive delete method. It takes a value as an input and deletes the node with that value if it exists. Each call `return` the new root of the three (or subtree) after the deletion.

Notice that in the test suite the `delete` method is called like this:

```py
bst = bst.delete(character)
```

1. Check if the current node is empty (has no value). If it is, return `None`. This represents an empty tree or a leaf node where deletion has already occured.

2. If the value to delete is less than the current node's value:
   1. If there's a left child, recursively delete the value from the left subtree and update the left child reference with the result.
   
   2. Return the current node.

3. If the value to delete is greater than the current node's value:
   1. If there's a right child, recursively delete the value from the right subtree and update the right child reference with the result.

   2. Return the current node.

4. If the value to delete equals the current node's value, we've found the node to delete:
   1. If there is no right child, return the left child. This bypasses the current node, effectively deleting it.

   2. If there is no left child, return the right child, accomplishing the same thing.

   3. If there are both left and right children:
      1. Start at the right child.

      2. Walk left until you find the smallest node in that right subtree. This is the next-largest value after the current node's value.

      3. Copy the next largest value into the current node's value.

      4. Delete that successor value from the right subtree.

      5. Call delete on the right subtree for that successor value, then save the returned node as the right child.

      6. Return the current node.

[Go to Code](CH10_L8_delete/main.py)

# Postorder Traversal

A "postorder" traversal also visits all the nodes in a tree. It's called "postorder" because the current node is visited after its children. The following tree:

```
    > 7
        > 6
> 4
    > 2
        > 1
```

Would be visited in this order

```
[1, 2, 6, 7, 4]
```

## Assignment
Our data team didn't like the way we ordered the users in our BST export (personally I think they just want to kick the work for themselves down the road). Anyhow, we've been asked to change it.

**Implement the recursive `postorder` method**. Here are the algorithm's steps:

1. Recursively traverse the left subtree
2. Recursively traverse the right subtree
3. Visit the value of the current node by appending its value to the visited array
4. Return array of visited nodes

[Go to Code](CH10_L12_postorder_traversal/main.py)

# Inorder Traversal

An "inorder" traversal is the most intuitive way to visit all the nodes in a tree. It's called "inorder" because the current node is visited between its children. It results in an ordered list of the nodes in the tree. The following tree:

```
    > 7
        > 6
> 4
    > 2
        > 1
```

Would be visited in this order:

```
[1, 2, 4, 6, 7]
```

## Assignment

Turns out, the data team had no idea what they were talking about, and our product lead just wanted an export of our tree in sorted order. He wants to be able to see the users in the order they signed up (and were thus given user IDs).

**Implement the recursive `inorder` method**. Here are the algorithm's steps:

1. [ ] Recursively traverse the left subtree
2. [ ] Visit the value of the current node by appending its value to the visited array
3. [ ] Recursively traverse the right subtree
4. [ ] Return the list of nodes visited so far

# Node Exists

On LockedIn, it's common for one user to navigate directly to another user's profile. We even creepily give the stalked user a notification that someone is looking at their profile.

To make this feature work, we need to be able to quickly check if a user exists in our tree.

## Assignment

**Complete the `exists` method.**

It should take a value as input and return `True` if the value exists in the tree, and `False` if it doesn't. It's a recursive method, as you probably guessed. 