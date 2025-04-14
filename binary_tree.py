# This algorythm creates a Binary Tree

class Node:
    def __init__(self, value: str):
        """Initialize A Node for A Binary Tree


        :param value: Value of the Node
        """
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self, value):
        """Insert into Node left Node

        :param value: Node value to be inserted to the left
        :return:
        """
        self.left = value

    def insert_right(self, value):
        """Insert into Node right Node

        :param value: Node value to be inserted to the right
        :return:
        """
        self.right = value


class BinaryTree:
    def __init__(self, root: Node):
        """

        :param root: Root Node for Binaryy Tree
        """
        self.root = root
        self.right = root.right
        self.left = root.left

    def insert_left(self, value: Node, base=None):
        """Inserts new Node to Binar Tree to the left

        :param value: Node to be inserted to the left side of the selected Node
        :param base: Base Node for recursion to make added Node be added at the end
        :return: self.insert_left(value, base)
        """
        if self.root.left is None:
            self.root.insert_left(value)
            self.left = value
        else:
            # self.root.left is not None, base is None
            if base is None:
                base = self.root.left
                return self.insert_left(value, base)
            if base.left is None:
                base.insert_left(value)
            else:
                return self.insert_left(value, base.left)

    def insert_right(self, value: Node, base=None):
        """Inserts new Node to Binar Tree to the right

        :param value: Node to be inserted to the right side of the selected Node
        :param base: Base Node for recursion to make added Node be added at the end
        :return: self.insert_right(value, base)
        """
        if self.root.right is None:
            self.root.insert_right(value)
            self.right = value
        else:
            if base is None:
                base = self.root.right
                return self.insert_right(value, base)
            if base.right is None:
                base.insert_right(value)
            else:
                return self.insert_right(value, base.right)

# A = Node(value="A")
# B = Node(value="B")
# C = Node(value="C")
# D = Node(value="D")
# E = Node(value="E")
# F = Node(value="F")
# G = Node(value="G")
#
# Binary_1 = BinaryTree(root=A)
#
# Binary_1.insert_left(B)
# Binary_1.insert_right(C)
# Binary_1.left.insert_left(D)
# Binary_1.left.insert_right(E)
# Binary_1.right.insert_right(G)
# Binary_1.right.insert_left(F)
#
# print(Binary_1.left.left.value)
# print(Binary_1.left.right.value)
# print(Binary_1.right.left.value)
# print(Binary_1.right.right.value)

#        A
#       / \
#      B   C
#     /\   /\
#    D  E  F G
