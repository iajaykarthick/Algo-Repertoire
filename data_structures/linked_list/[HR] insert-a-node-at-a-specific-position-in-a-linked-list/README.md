## Insert a node at a specific position in a linked list

[Hackerrank](https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/)

Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  `data` attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

## Solution
```python
def insertNodeAtPosition(llist, data, position):
    curr = llist
    i = 0
    while curr and i < (position-1):
        curr = curr.next
        i += 1
    temp = curr.next
    new_node = SinglyLinkedListNode(data)
    curr.next = new_node
    new_node.next = temp
    return llist
```