class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = []

    def insertVt(self, vertex):
        if vertex.vertex != self.vertex:
            self.next.append(vertex)
        else:
            print("Cannot insert a vertex with the same value as the current vertex")

class GraphSearch:
    def __init__(self, startNum):
        self.fVer = Vertex(startNum)
        self.edges = {startNum: self.fVer}

    def linkVertex(self, linkedNum, linkNum):
        if linkedNum in self.edges:
            if linkNum not in self.edges:
                self.edges[linkNum] = Vertex(linkNum)
            linked_vertex = self.edges[linkedNum]
            link_vertex = self.edges[linkNum]
            linked_vertex.insertVt(link_vertex)
        else:
            print(f"Cannot find vertex {linkedNum}")

    def adjacentList(self, vtNum):
        if vtNum in self.edges:
            vertex = self.edges[vtNum]
            adjacent_vertices = [v.vertex for v in vertex.next]
            print(f"Adjacent list for vertex {vtNum} = {adjacent_vertices}")
        else:
            print(f"Cannot find vertex {vtNum}")

    def depthFirstSearch(self, startNum):
        if startNum not in self.edges:
            print(f"Cannot find vertex {startNum}")
            return
        visited = set()
        self._dfs_recursive(startNum, visited)

    def _dfs_recursive(self, currentNum, visited):
        if currentNum not in visited:
            print(currentNum, end=' ')
            visited.add(currentNum)
            current_vertex = self.edges[currentNum]
            for neighbor in current_vertex.next:
                self._dfs_recursive(neighbor.vertex, visited)





graph = GraphSearch(1)
graph.linkVertex(1, 2)
graph.linkVertex(1, 3)
graph.linkVertex(2, 4)
graph.linkVertex(3, 4)
graph.linkVertex(4, 5)
graph.adjacentList(1)
graph.adjacentList(2)
graph.adjacentList(3)
graph.adjacentList(4)
graph.adjacentList(5)


graph.depthFirstSearch(1)