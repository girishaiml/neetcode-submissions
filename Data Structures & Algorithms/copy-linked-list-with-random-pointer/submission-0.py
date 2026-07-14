# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = x
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copies = {}

        # First pass: create a copy of every node
        current = head
        while current:
            copies[current] = Node(current.val)
            current = current.next

        # Second pass: connect next and random pointers
        current = head
        while current:
            copied_node = copies[current]

            copied_node.next = copies.get(current.next)
            copied_node.random = copies.get(current.random)

            current = current.next

        return copies[head]