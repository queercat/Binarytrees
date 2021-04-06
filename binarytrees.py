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

    def print_tree(self, root_node):
        if root_node == None:
            return

        print(root_node.val)
        
        self.print_tree(root_node.left)
        self.print_tree(root_node.right)

        return root_node.val

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
    tree.print_tree(tree.root_node)

if __name__ == "__main__":
    main()