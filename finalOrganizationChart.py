# 부서, 직급, 번호, 이름
# 직급 : 사장, 부장, 과장, 대리, 사원
# 부서 : 인사, 경영, 연구, 영업
# 번호 : 인덱스



class Node:
    def __init__(self, node):
        self.node = node
        self.nextNode = {}
        self.branchNumber = 0

# nextNode는 node보다 큰 숫자여야 함
# node, nextNode는 중복되면 안됨

    def ConnectNode(self, node, nextNode):
        self.branchNumber += 1


class OrganizationChart:
    def __init__(self, root):
        self.root = root


    def InsertNode(self, node, nextNode):

