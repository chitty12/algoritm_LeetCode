class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next=[]

    def insertVt(self, number):
        if number != self.vertex:
            self.next.append(number)
        else:
            print("can not insert number same with vertex")

class GraphSearch:
    def __init__(self, startNum):
        self.fVer = Vertex(startNum)
        self.edges = {startNum : self.fVer}

    def linkVertex(self, linkedNum, linkNum):
        if linkedNum in self.edges:
            new_vertex = Vertex(linkNum)
            self.fVer.insertVt(new_vertex)
        else:
            print(f"can not search {linkedNum} Vertex")

    def adjacentList(self, vtNum):
        if vtNum in self.edges:
            
            print(f"adjacent List = {self.fVer.next}")
