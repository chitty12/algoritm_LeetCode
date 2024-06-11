# 부서, 직급, 번호, 이름
# 직급 : 사장, 부장, 과장, 대리, 사원
# 부서 : 인사, 경영, 연구, 영업
# 번호 : 인덱스


class Node:
    def __init__(self, department, position, number, name):
        self.department = department
        self.position = position
        self.number = number
        self.name = name
        self.nextNode = []

   # nextNode는 node보다 큰 숫자여야 함
   # node, nextNode는 중복되면 안됨
    def ConnectNode(self, nextNode):
        if nextNode.number > self.number and nextNode not in self.nextNode:
            self.nextNode.append(nextNode)
        else:
            print("잘못된 nextNode입니다.")


class OrganizationChart:
    def __init__(self, root_department, root_position, root_number, root_name):
        self.root = Node(root_department, root_position, root_number, root_name)
        self.nodes = {root_number: self.root}
    
    def InsertNode(self, node_department, node_position, node_number, node_name, nextNode_number):
        if nextNode_number in self.nodes:
            parent_node = self.nodes[nextNode_number]
            new_node = Node(node_department, node_position, node_number, node_name)
            parent_node.ConnectNode(new_node)
            self.nodes[node_number] = new_node
        else:
            print(f"{nextNode_number}는 존재하지 않는 노드입니다.")

    def printOrganizationChart(self, node, depth=0):
        if node:
            print("  " * depth + f"- {node.department} {node.position} {node.number}: {node.name}")
            for next_node in node.nextNode:
                self.printOrganizationChart(next_node, depth + 1)



# Organization Chart 생성
org_chart = OrganizationChart("the Top", "사장", 1, "홍길동")

# 노드 추가
org_chart.InsertNode("경영", "부사장", 2, "김철수", 1)  
org_chart.InsertNode("인사", "인사부장", 3, "이영희", 1)
org_chart.InsertNode("연구", "연구부장", 4, "박민수", 1)   
org_chart.InsertNode("영업", "영업부장", 5, "정기호", 1)  
org_chart.InsertNode("경영", "과장", 6, "이민호", 2)  
org_chart.InsertNode("경영", "과장", 6, "박지현", 2)  
org_chart.InsertNode("인사", "과장", 8, "정승환", 3)
org_chart.InsertNode("연구", "과장", 9, "임현주", 4)   
org_chart.InsertNode("연구", "과장", 9, "이미주", 4)   
org_chart.InsertNode("영업", "과장", 10, "최성준", 5)  
org_chart.InsertNode("경영", "대리", 11, "김진우", 6)  
org_chart.InsertNode("경영", "대리", 11, "한영호", 6)  
org_chart.InsertNode("인사", "대리", 12, "박찬호", 8)
org_chart.InsertNode("인사", "대리", 12, "김희철", 8)
org_chart.InsertNode("인사", "대리", 12, "김영호", 8)
org_chart.InsertNode("연구", "대리", 13, "정미숙", 9)   
org_chart.InsertNode("연구", "대리", 13, "김지원", 9)   
org_chart.InsertNode("연구", "사원", 13, "이지훈", 9)   
org_chart.InsertNode("영업", "사원", 14, "정기호", 10)  
org_chart.InsertNode("영업", "사원", 14, "신지수", 10)  




org_chart.printOrganizationChart(org_chart.root)