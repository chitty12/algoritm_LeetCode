class Node:
    def __init__(self, value, nextNode):
        self.root = value
        self.left = Node.connect_left_node(self, nextNode)
        self.right = Node.connect_right_node(self, nextNode)

    def connect_left_node(self, value):
        if(self.root > value):
            return value
        elif self.root == value:
            return print("value error")
        else:
            return None
    def connect_right_node(self, value):
        if(self.root < value):
            return value
        elif self.root == value:
            return print("value error")
        else:
            return None

    def search_tree(self, value):
        if self.root > value:
            Node.search_tree(self, self.left)
        elif self.root == value:
            print(f"got find node {value}!")
        else:
            Node.search_tree(self, self.right)

    def delete_tree(self, value):
        