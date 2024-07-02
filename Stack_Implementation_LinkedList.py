class Stack:
    class Node:
        def __init__(self, data):
            self.data = data # store the data in this node
            self.next = None # initialize the next node as None

    def __init__(self):
        self.top = None # initialize the top of the stack as None

    def pop(self):
        if self.top is None:
            raise IndexError("stack is empty")
        item = self.top.data # store the top item's data
        self.top = self.top.next # update the top to be the next node
        return item # return the popped item

    def push(self, item):
        t = self.Node(item) # create a new node with the provided data
        t.next = self.top # set the next of the new node to be the current top
        self.top = t # update the top to be the new node

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None # return True if the stck is empty, false otherwise





