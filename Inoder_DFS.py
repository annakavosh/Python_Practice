## indored traversal
## Left - Root - Right
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def Inorder(root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif (stack):
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right

        else:
            break

    print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    Inorder(root)

