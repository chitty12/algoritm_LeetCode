# 부서, 직급, 번호, 이름
# 직급 : 사장, 부장, 과장, 대리, 사원
# 부서 : 인사, 경영, 연구, 영업
# 번호 : 인덱스



class Node:
    def __init__(self, node):
        self.node = node
        self.nextNode = {}
        self.branchNumber = 0

    def connect_node(self, nextNode):
        if nextNode.node > self.node and nextNode.node not in self.nextNode:
            self.branchNumber += 1
            self.nextNode[nextNode.node] = nextNode

class OrganizationChart:
    def __init__(self, root):
        self.root = root
        self.nodes = {root.node: root}

    def insert_node(self, node, nextNode):
        if node in self.nodes and nextNode not in self.nodes:
            new_node = Node(nextNode)
            self.nodes[node].connect_node(new_node)
            self.nodes[nextNode] = new_node

# 조직도 생성 예제
# 직급: 사장(0), 부장(1), 과장(2), 대리(3), 사원(4)
# 부서: 인사(0), 경영(1), 연구(2), 영업(3)
# 번호: 인덱스
root = Node(0)  # 사장 노드
chart = OrganizationChart(root)

# 노드 삽입 예제
chart.insert_node(0, 1)  # 사장 -> 부장
chart.insert_node(1, 2)  # 부장 -> 과장
chart.insert_node(2, 3)  # 과장 -> 대리
chart.insert_node(3, 4)  # 대리 -> 사원

# 노드 확인
def print_chart(node, level=0):
    print("  " * level + f"Node {node.node}")
    for next_node in node.nextNode.values():
        print_chart(next_node, level + 1)

print_chart(chart.root)



class Node:
   def __init__(self, node):
       self.node = node
       self.nextNode = {}
       self.branchNumber = 0

   # nextNode는 node보다 큰 숫자여야 함
   # node, nextNode는 중복되면 안됨
   def ConnectNode(self, node, nextNode):
       if nextNode > node and nextNode not in self.nextNode.values():
           self.nextNode[self.branchNumber] = nextNode
           self.branchNumber += 1
       else:
           print("잘못된 nextNode입니다.")

class OrganizationChart:
   def __init__(self, root):
       self.root = Node(root)
       self.nodes = {root: self.root}

   def InsertNode(self, node, nextNode):
       if node in self.nodes:
           parent_node = self.nodes[node]
           new_node = Node(nextNode)
           parent_node.ConnectNode(node, nextNode)
           self.nodes[nextNode] = new_node
       else:
           print(f"{node}는 존재하지 않는 노드입니다.")