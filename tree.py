# Python의 class를 이용해 직접 구현하기

# 구현 조건

# - 루트(Root): 부모가 없는, 가장 상윗단의 노드
# - 노드(Node): 트리 구조의 자료 값을 담고 있는 요소
# - 에지(Edge): 노드 간의 연결선
# - 부모(Parent): 연결된 두 노드 중 더 상위에 있는 노드
# - 자식(Child): 연결된 두 노드 중 하위에 있는 노드
# - 경로(Path): 두 노드를 연결하는 에지의 시퀀스
# - 잎새 노드(Leaf Node): 자식 노드가 없는 노드
# - 내부 노드(Internal Node): 잎새 노드를 제외한 모든 노드
# - 레벨, 깊이(Level, Depth): 루트 노드로부터의 경로의 길이
# - 트리의 높이(Height): 트리에서 가장 큰 레벨 값

# value, left, right를 가진 node class를 이용하여 구현한다.
# 다음과 같은 트리의 연산을 구현해야 한다. (자료의 입력과 삭제는 구현하지 않는다.)
# 순회 알고리즘: 순회하는 순서대로 Element를 출력한다.
# 깊이 우선 순회 (Preorder, Depth-First Traversal)
# 대칭 순회 (Inorder, Symmetric Traversal)
# 후위 순회 (Postorder)
# 탐색 알고리즘: 탐색하여 Tree에 해당 value의 존재 여부를 판단한다.
# 너비 우선 탐색 (Breadth-First Search; BFS)
# 깊이 우선 탐색 (Depth-First Search; DFS)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = Node(root) if root is not None else None
    
    def preorder_traversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    def search(self, value, node):
        if node is None:
            return False
        if node.value == value:
            return True
        return self.search(value, node.left) or self.search(value, node.right)
