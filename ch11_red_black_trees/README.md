# Unbalanced Trees

BSTs have a problem. While it's true that on average a `BST` has `O(log(n))` lookups, deletions, and insertions, that fundamental benefit can break down quickly.

If mostly sorted data, or even worse, completely sorted data, is inserted into a binary tree, the tree will be much deeper than it is wide. As you know by now, the Big O complexity of the tree's operations depend entirely on the depth of the tree. 

# Red-Black Tree

A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

## How it works

Each node in a RB Tree stores an extra bit, called the "color": either red or black. The "color" ensures that the tree remains approximately balanced during insertions and deletions. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

```
The "red" and "black" nomenclature is arbitrary - you could call them "red vs blue" trees (shout-out rooster teeth), or not even call it "color" at all. The important part is just that we now have two "types" of nodes and that will affect the algorithm for balancing it.
```

**List of Very Simple Rules**

- Each node is either red or black
- The root is black
- All Nil leaf nodes are black
- If a node ir red, then both it children are black
- All paths from a single node go through the same number of black nodes to reach any of its descedant Nil (black) nodes.

## Assignment

As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

In a normal `BST`, the child nodes don't need to know about, or carry a reference to their parent. The same is not true for Red-Black trees.

The `RBNode` class is already implemented for you, as well as the `__init__` constructor method of the `RBTree` class. There's also a data member, `self.nil` created for you in the constructor. `self.nil` contains the value we'll use to designate all the `nil` (empty) leaf nodes, which are used for rebalancing purposes but contain no "actual" value.

**Complete the `insert` method**. It should take a value as input and add the value as a new node in the tree if the value doesn't already exist.

1. [ ] Create the `new_node`:
    1. [ ] Create a new `RBNode` from the given input value
    2. [ ] The `new_node` shouldn't have a parent yet
    3. [ ] The `new_node`'s left and right children should be `nil`
    4. [ ] The `new_node` is red. (`new_node.red = True`)
2. [ ] Find the parent of the `new_node` if there will be one:
    1. [ ] Initialize a `parent` variable to `None`
    2. [ ] Initialize a `current` variable to the root node of the tree
    3. [ ] While `current` isn't a nil node:
        1. [ ] Set `parent` to the `current`
        2. [ ] If the `new_node`'s value is less than the `current` node's, set `current` to its own left child. If `new_node`'s value is greater, set `current` to its own right child. If the values are equal, just `return` because this value is a duplicate.
    4. [ ] If you followed the steps correctly, `parent` will be a reference to the node that will become the parent of the `new_node`
3. [ ] Insert the `new_node` by setting the parent's child:
    1. [ ] Set the `new_node`'s parent to the parent we just found
    2. [ ] If the parent is `None`, we are dealing with a new root, so set the tree's `root` data member to the `new_node`
    3. [ ] Otherwise, compare the values of the parent and `new_node` and set the parent's `left` or `right` child based on the results

We're done for now! We've _really_ just made another (more complicated) regular binary tree, seeing as it's not a fully-fledged red-black tree yet... but these upgrades will allow us to implement the rest of the logic in the next few lessons.

So far we've added:

- a `parent` pointer from child to parent (so children know who their parents are)
- the mechanisms for coloring the nodes, but have defaulted them all to `red` for now

## Tip

I'd highly recommend using pencil/paper or some kind of drawing tool to visualize the tree as you go through the assignments in this chapter.