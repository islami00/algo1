## The node
This is a data structure that stores a value and a reference to other node(s).
i.e either the node after it (in a single linked list) or the one after and before it (in a double linked list)

## The head
This is a special node that does not reference an element before it.

It is the only node the list has a reference to
Since every other node points to the next node, we can start from there and find any node.
this is called list traversal

## The tail

This is a special node that has no next node reference.


## Single linked list


THis is a collection of nodes with the head being the only node that is explicitly stored in memory.
Each node in the list passes references to the next node till the tail which terminates the linked list.