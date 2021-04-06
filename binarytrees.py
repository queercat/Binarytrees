""" Example Binary Tree
"      1
"     / \
"    3   4
"   / \   \
"  5   6   2
"           \
"            7
"""

class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def append(node):
        self.right = node

        return self.right

    def getFirst(linked_list):
        while(linked_list.left != None):
            linked_list = linked_list.left

        return linked_list

class Tree:
    def __init__(self, root_node = None):
        self.root_node = root_node

    def printTree(self, root_node):
        if root_node == None:
            return

        print(root_node.val)
        
        self.printTree(root_node.left)
        self.printTree(root_node.right)

        return root_node.val

    def reverseTree(self, root_node):
        if root_node == None:
            return

        root_node.left, root_node.right = root_node.right, root_node.left

        self.reverseTree(root_node.left)
        self.reverseTree(root_node.right)

        return root_node

    def isInTree(self, root_node, value):
        if root_node == None:
            return

        if root_node.val == value:
            return True

        if self.isInTree(root_node.left, value) == True or self.isInTree(root_node.right, value) == True:
            return True

        return False

def createNodes():
    root_node = Node(1)

    left_child0 = Node(3)
    left_child0_right = Node(6)
    left_child1 = Node(5)

    right_child0 = Node(4)
    right_child1 = Node(2)
    right_child2 = Node(7)

    root_node.left = left_child0
    left_child0.left = left_child1
    left_child0.right = left_child0_right

    root_node.right = right_child0
    right_child0.right = right_child1
    right_child1.right = right_child2

    return Tree(root_node)

def main():
    tree = createNodes()
    
if __name__ == "__main__":
    main()