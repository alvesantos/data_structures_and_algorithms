## Goals

- Learn to think algorithmically
  - Break problems down into easier-to-solve parts
- Learn to think about how to organize data for more efficient access. Break problems down into data models that make sense
- Learn and practice performance optimization. Make your code run faster and more efficiently, even with more data.
## What is Data Structure?

Organizational tools that allow for more advanced algorithms.

- Lists (Ordered collections of data)
- Dictionaries (Key -> value mappings)
- Sets (Unordered collections of unique data)
## What is Algorithm

Set of instructions that can be carried out to solve a problem. People use algorithms all the time without even realizing it. Practically every function you write in code is an algorithm.
# Insert Review

Inserting into a binary search tree (like most of its operations) is very fast. Picture the algorithm that you just wrote in your head: how many comparisons does it take to find the right spot for a new node?

It only required one comparison for each level of thre tree, making it `O(log(n))`! (At least in a balanced tree, we'll tal about this later).

Order `log(n)` is very fast - it's practically as good as `O(1)` in most cases. If our tree has `1,000,000` nodes, we only need to make `20` comparisons to find the right spot for a new node. If our tree is 2x larger (`2,000,000` nodes), we only need to make one more comparison per insert, `21` total.
# Min and Max
Some of the simpler BST algorithms are the `get_min` and `get_max` methods.
## Assignment

Now that we can add users to our BST, our systems team wants us to start implementing search functionality.

Implement the `get_min` and `get_max` methods. They should return the minimum and maximum values in the BST respectively.
### Tips
- the `get_min` function loops through all the `left` child nodes and returns the value of the last one.
- the `get_max` function does the same for the right children.
[Go To Code](ch10_binary_trees/CH10_L7_min_and_max/main.py)

# Deletion Review

The `delete` method is `O(log(n))` because, like most binary tree operations, we don't have to search the entire tree. We only have to search one path from the root to the left node we want to delete.

The depth of the tree on average is equal to `log base 2` of the number of nodes in the tree. For example:

|Nodes|Depth|
|---|---|
|1|0|
|2|1|
|4|2|
|8|3|
|16|4|
|32|5|
|64|6|
|128|7|
|256|8|
|512|9|
|1024|10|
|2048|11|
|4096|12|

**We only need to use ~10 steps to delete a node from a tree of ~1000 nodes**.

# Preorder Traversal

A "Preorder" travessal is a way to visit all the nodes in a tree. It's called "preorder" because the current node is visited before its children. This tree:

```
    > 7
        > 6
> 4
    > 2
        > 1
```

Would be traversed in this order:

```
[4, 2, 1, 7, 6]
```

Sometimes it's useful (albeit a bit slow) to iterate over all the nodes in the tree. In the case of LockedIn, we've been asked to build a way to create a backup of our database indexes - this traversal will allow us to save all the data in the tree to a file.

## Assignment

Implement the recrusive `preorder` method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.

For example, the first call to `preorder` on an entire tree would be:

```python
# an empty list is passed in the first call
bst_node.preorder([])
```

Here are the algorithm's steps:

1. [ ] If the current node actually contains a value (`self.val` is not `None`), visit it by appending its value to the visited array
2. [ ] Recursively traverse the left subtree
3. [ ] Recursively traverse the right subtree
4. [ ] Return the array of visited nodes