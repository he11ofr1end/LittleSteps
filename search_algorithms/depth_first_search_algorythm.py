from trees.binary_tree import BinaryTree


class DepthFirstSearch:
    def __init__(self, binary_tree: BinaryTree, value: str):
        """Initialize DepthFirst Search

        :param binary_tree: The Binary Tree to be searched
        :param value: The value to be searched
        """
        self.binary_tree = binary_tree
        self.value = value
        self.stack = Stack()
        self.k = 0

    def run(self, root=None) -> str:
        """Run depth first search

        :param root: root Node from where to start the search
        :return: str
        """
        # if root is None, set the first root
        if root is None:
            root = [(self.binary_tree.root, self.k)]

        # Add to stack root Nodes
        self.add_to_stack(root)

        # Pop from stack last added value
        pop_node = self.pop_from_stack()

        # if we have found the result than return k depth and the value
        if pop_node[0].value == self.value:
            return f"Node {self.value} is on {pop_node[1]} depth"

        root = self.change_root(pop_node)

        # check if stack is fully empty and no node was found
        if len(pop_node) == 0:
            return f"Node {self.value} is NOT in binary tree"
        return self.run(root)

    def add_to_stack(self, root: list[Node, int]) -> None:
        """Method to add Node to stack.

        :param root: Nodes to add
        :return:
        """
        # Adding to stack
        for e_node in root:
            self.stack.add(e_node)

    def pop_from_stack(self) -> tuple[Node, int]:
        """Pop Node from stack.

        :return:
        """
        # Popping and checking
        pop_node = self.stack.pop()
        return pop_node

    @staticmethod
    def change_root(pop_node: tuple[Node, int]) -> list[tuple[Node, int]]:
        """Change root to continue depth search

        :param pop_node: Popped from stack Node
        :return: list((Node, int))
        """
        root = []
        # Check left Node if not None - add
        if pop_node[0].left is not None:
            root.append((pop_node[0].left, pop_node[1] + 1))

        # Check right Node if not None - add
        if pop_node[0].right is not None:
            root.append((pop_node[0].right, pop_node[1] + 1))
        return root


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        """Adds to stack values

        :param value: Value to be added to stack
        :return:
        """
        self.stack.append(value)

    def pop(self):
        """Pop element from stack

        :return:
        """
        return self.stack.pop(len(self.stack) - 1)
