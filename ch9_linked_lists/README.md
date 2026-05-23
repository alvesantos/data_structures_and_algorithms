# Linked Lists

Remember how the `push` method on our Queue is `O(n)` insted of `O(1)`?

```py

def push(self, item):
    # everything is self.items has to shift
    # up a position, which takes O(n) time

    self.items.insert(0, item)
```

Let's fix that.

To build a faster queue, we'll use a Linked List instead of a regular List (array) under the hood. A linked list is where elements are not stored next to each other in memory, instead, each item references the next in a chain.

## Nodes

Our nodes will be represented by a simple class with two fields:

- val - The raw string value that the node holds (e.g. 'Carla', 'James', etc)
- next - A reference to the next node in the list.

### Assignment

Let's lock-in and make LockedIn faster!

1. Complete the Node's constructor.
   1. Set its `val` field to the provided value.
   2. Set its next field to None
2. Complete the `Node`'s `set_next` method. It should set the next field to the provided node.

# Linked List vs. List

A linked list is a collection of ordered items, so it's similar to a "normal" list (also called an "array" or "slice" in other languages).

Items in a "normal" list are stored next to each other in memory, and to get an item from a normal `List` we have to use a numbered index:

```py
car = cars[3]
```

You can think of the "index" as simply an offset from the start. The `cars` list in this example refers to the start of the list, and `3` is just the 4th item in that section of memory. With a normal list, all the data is stored in the same place in memory and the index is just a way to find the right spot.

In a linked list, there are no indexes! Each node contains two things: the data itself, and a reference to the next node in the list. Iterating over a linked list requires starting at the head node and following the next references until you reach the end.

```py
current_car_node = head_card_node

while current_car_node is not None:
    print(current_car_node.val)
    current_car_node = current_car_node.next
```

Frankly, linked lists can be annoying to use and incur more overhead, so why use a linked list at all? It's because sometimes linked lists are much faster to make updates to, particularly when inserting or deleting items from teh middle.

In a normal list, if you insert an item in the middle, you have to shift all the items after it down one spot, which take `O(n)` time

In a linked list, once you've traversed to a given node, insertion i `(O(1))` because you can simply update two references

# Iterating

Even though iterationg with linked lists kinda sucks compared to the simplicity of arrays (normal lists), we've got to do it. Although the implementation is more complex and slow, we can still make it easy for users of our class by providing an **iter** method

## The yield Keyword

The `yield` keyword in Python returns a value, kind of like return. However, it's used to turn the function into a generator function.

A generator function creates a new function object. When that function is called, it executes the code in the generator function until it hits a `yield` statement. At that point, the function puases and returns the value of the `yield` statement. The next time the function is called, it picks up right where it left off.

```py
def create_message_generator():
    yield "hi"
    yield "there"
    yield "friend"

gen = create_message_generator()
first = next(gen)
print(first) # hi
second = next(gen)
print(second) # there
third = next(gen)
print(third) # friend
```

Every time you call create_message_generator(), it creates a new generator instance. To continue from when you left off, you nedd to assign this generator to a variable (like gen in the example above). This way, when you use next() or loop over the generator, you're continuing with the same instance rather than strating a new one.

## Assignment

The `LinkedList` class is a wrapper class that users the `Node` class we already wrote.

1. Complete the `__init__` method. It should set the `head` field to `None`.

No other node points to the linked list's `head` (first) node, so the `LinkedList` class itself nedds to keep track of it. We'll use the term `head` and `tail` like this:

`head node` -> `node` -> `node` -> `node` -> `tail node`

The direction of flow above might feel opposite to what you're used to with a `Queue`, but it's really the same. Above I'm using arrows to show which nodes are pointing to which other nodes. In a future lesson when we implements a `Queue` using a `LinkedList`, we'll add elements to the `tail` and remove elements from the `head`.

2. Complete the `__iter__` method. It should be a generator function that `yield`s each node in the linked list, from the `head` to the `tail`.
   - Create a reference to the `head` node (e.g. `node = self.head`)
   - Use a `while` loop to iterate over the linked list until `node` is `None`
     - Yield the current `node`
     - Set `node` to the `next` node

We need to change which node is the next to be yielded, but the `set_next` method of the `Node` class changes which is the next to be pointed to - don't use it.

By overriding the `__iter__` method, Python will allow us to use a `for` loop to iterate over the linked list:

```py
from node import Node

ll = LinkedList()
ll.head = Node("first")
ll.head.next = Node("second")
ll.head.next.next = Node("third")

for node in ll:
    print(node.val)
```

[Go to the code](CH9_L4_iterating.py/main.py)

# Add to Tail

Time to allow our `LinkedList` to add new nodes to the end of the list. Kind of like a regular Python List's `.append` method.

## Assignment

Complete the `add_to_tail` method. It adds a new node to the end of the list and returns nothing.

1. If the isn't a `head` node, set the new node as the `head` and return.
2. Otherwise, keep a reference to the "last" node in the list - start with it set to the `head`.
3. Iterate over the linked list (you can use a `for` loop now that you've added your own `__iter__`!)
   - Update your "last" node reference to the current node
4. Once you've iterated over the entire list. your "last" reference should be the last node in the list (the "tail"). Set the `next` field of the "last" node to the new node.

[Go to Code](./CH9_L5_add_to_tail/main.py)

# Add to Head

For added flexibility, let's allow users to add items to the front of our linked list as well.

## Assignment

Implement the `add_to_head` method. It should add a new node to the front of the list and return nothing.

1. Set the "next" field fo the given node to the current head node.
2. Update the head reference to the given node.

[Go to Code](./CH9_L6_add_to_head/main.py)

# Linked List Queue

To use our Linked List as a fast queue (`O(1) pushes and pops`) we need our `add_to_tail` function to be `O(1)`. Currently, it iterates over the entire list before appending an item. We can fix this by keeping track of the last item with a new data member: `tail`.

Node: It's common in algorithms to make this kind of trade-off. By using a litle extra memory (keeping track of `tail`), we can make our operations faster. Sometimes you might need to go the other way, and use more computation time to save memory.

## Assignment

LockedIn's queue was working just fine on small datasets, but appending items once the lsit has 100,000+ items has started to take a toll on our servers. Implement these changes to speed up our Linked List's inserts to `O(1)`:

1. Update the constructor to `self.tail` to `None`.
2. Update `add_to_head` to also set the `tail` reference to the given node if the list is empty.
3. Update `add_to_tail`:
   1. Set the head and tail to the given node if the list empty.
   2. Instead of iterating through the list to find the last node, use the `tail` node to append the new node (for example, set `self.tail.next` to the new node).
   3. Update the `tail` reference to new node.

[Go to Code](./CH9_L7_linked_list_queue/main.py)

# Remove from Head

We're one method away from having a fully functioning `O(1)` Queue! We just need a way to remove the first element from the linked list in constant time. When we're finished, our `LinkedList` will fulfill the basic requirements of a Queue:

- `add_to_tail`: Constant time insert
- `remove_from_head`: Constant time pop

Let's rename the `LinkedList` class to `LLQueue` and remove the `add_to_head` functionality because Queues don't allow inserting into the wrong end.

We've also flipped the arrows in the printed representation to reflect the change.

## Assignment

Complete the `remove_from_head` method. It should remove the first node from the list (the head) and return it.

1. If the list is empty, just return None.
2. Assign the head to be removed to a variable.
3. Set the list's head to the next node in the list.
4. If the list became empty, set th list's tail to `None`.
5. Set the (now removed) head's `next` to `None`. We don't want it to point do any node in the list.
6. Return the removed head.

[Go to code](CH9_L8_remove_from_head/main.py)

# Linked List Queue Quiz

Let's recap a few key points about linked lists and queue:

1. The problem with our array (normal Python list) implementation of a queue was that it had `O(n)` push operations.
2. The linked list implementation of a queue has `O(1)` push operations.
3. Linked lists are usually a worse choice than standard arrays because:
   - They are less performant due to more memory overhead
   - They are more complex to work with, debug, and reson about
   - They have no random access (indexing to a specific element)
4. Doubly linked lists are a better choice than arrays in very specific circumstances because they have `O(1)` insertions and deletions at both ends of the list.
