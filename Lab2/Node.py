class Node:
    def __init__(self, v):
        self.__value = v
        self.__left = None
        self.__right = None

    def getValue(self):
        return self.__value

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self, r):
        self.__right = r

    def setLeft(self, l):
        self.__left = l

    def __str__(self):
        return str(self.__value)