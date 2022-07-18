class Graph:
    def __init__(self):
        self.adj_list = {}
        ## initiating a adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        ## V1 and V2 are the 2 vertices that are being connected
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: ##this is for edge case where vertex exists but there is no connection between v1 and v2
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            l = self.adj_list[vertex]
            for i in l :
                self.adj_list[i].remove(vertex)
            self.adj_list.pop(vertex)
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list :
            print(f"{vertex} : {self.adj_list[vertex]}")


mygraph = Graph()
mygraph.add_vertex("A")
mygraph.add_vertex("B")
mygraph.add_vertex("C")
mygraph.add_vertex("D")
mygraph.add_edge("A", "B")
mygraph.add_edge("C", "A")
mygraph.add_edge("D", "B")
mygraph.add_edge("D", "C")
mygraph.print_graph()
print("---------")
mygraph.remove_edge("D", "B")
mygraph.print_graph()
print("---------")
mygraph.remove_vertex("D")
print("---------")
mygraph.print_graph()

