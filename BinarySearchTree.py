class Node:
    def __init__(self, value, leftNode=None, rightNode=None):
        self.root = value
        self.left = self.connect_left_node(leftNode)
        self.right = self.connect_right_node(rightNode)

    def connect_left_node(self, value):
        if value is not None:
            if self.root > value:
                return value
            elif self.root == value:
                print("Value error")
                return None
            else:
                return None
        else:
            return None

    def connect_right_node(self, value):
        if value is not None:
            if self.root < value:
                return value
            elif self.root == value:
                print("Value error")
                return None
            else:
                return None
        else:
            return None

class BinarySearchTree:
    def __init__(self):
        self.root = None

 
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value, None, None)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value, None, None)
            else:
                self._insert(value, node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _remove(self, value, node):
        if node is None:
            return None
        if value < node.root:
            node.left = self._remove(value, node.left)
        elif value > node.root:
            node.right = self._remove(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            min_node = self._find_min(node.right)
            node.root = min_node.value
            node.right = self._remove(min_node.value, node.right)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node