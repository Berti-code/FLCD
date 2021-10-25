from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, param):
        if self.root is None:
            self.root = Node(param)
        else:
            p = None
            leftFlag = False
            node = self.root
            while node is not None:
                p = node
                if node.getValue()[1] < param[1]:
                    node = node.getLeft()
                    leftFlag = True
                elif node.getValue()[1] > param[1]:
                    node = node.getRight()
                    leftFlag = False
            if  leftFlag == True:
                p.setLeft(Node(param))
            else:
                p.setRight(Node(param))

    def search(self, val):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.getValue()[1] > val:
                node = node.getLeft()
            elif node.getValue()[1] < val:
                node = node.getRight()
            else:
                return node.getValue()
        return None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.getLeft(), level + 1)
            print(' ' * 12 * level, node.getValue())
            self.printTree(node.getRight(), level + 1)

    def print(self):
        self.printTree(self.root)