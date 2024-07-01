
### Remove Nodes From LinkedList
"""
Given the head node of a singly linked list, modify the list such that any node that
has a node with a greater value to its right gets removed. Return the head of modified list.
"""
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def removeNodes(self, head):
        stack = [] # monotonic stack to store nodes in descending order
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop() # remove the nodes that are smaller than the current node
            if stack:
                stack[-1].next = current # update the next pointer to point to the top
            stack.append(current) # push current node to the stack
            current = current.next

        return stack[0] if stack else None

# testing linked list 5 -> 3 -> 7 -> 1
solution = Solution()

head1 = Node(5)
head1.next = Node(3)
head1.next.next = Node(7)
head1.next.next.next = Node(2)
head1.next.next.next.next = Node(1)
node = solution.removeNodes(head1)

while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next
