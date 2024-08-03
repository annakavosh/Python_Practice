from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode( {self.value})"


class Solution:
    def traverse(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root) # push root to the queue
        print("out of while loop len of queue: ",len(queue))
        while queue:
            print("in while loop len of queue: ", len(queue))
            levelSize = len(queue)
            currentLevel = []
            for i in range(levelSize):
                currentNode = queue.popleft()
                print(f"in for loop iter {i} len of queue: ", len(queue))
                # add the bode to the current level
                currentLevel.append(currentNode.value)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                    print(f" in for loop after left child append iter {i} len of queue: {len(queue)}")
                if currentNode.right:
                    queue.append(currentNode.right)
                    print(f" in for loop after right child append iter {i} len of queue: {len(queue)}")
            print("nodes in queue ", queue,"\n\n")

            result.append(currentLevel)

        return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(sol.traverse(root)))


main()
