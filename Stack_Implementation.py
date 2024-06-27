class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1 #initialize the top pointer to -1, indicating an empty stack

    def push(self, data):
        if self.top == len(self.stack) - 1:
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = data # add the data to current top position

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        data = self.stack[self.top]
        self.stack[self.top] = None # remove the data by setting it to None
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1



