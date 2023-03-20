class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._add(self.root, key, value)

    def _add(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._add(node.left, key, value)
                
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._add(node.right, key, value)
                
        else:
            node.value = value

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def update(self, key, value):
        node = self._find_node(self.root, key)
        if node is not None:
            node.value = value

    def _find_node(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._find_node(node.left, key)
        else:
            return self._find_node(node.right, key)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(f"{node.key}: {node.value}")
            self._print_tree(node.right)

