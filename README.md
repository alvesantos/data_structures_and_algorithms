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

