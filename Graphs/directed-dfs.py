class Graph:
    def __init__(self):
        self.graph = {}
        self.cycle = False
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def dfs_traversal(self, s, visited):
        if s in visited:
            return 
        visited.add(s)
        print(s)
        if s in self.graph:
            for adj in self.graph[s]:
                self.dfs_traversal(adj, visited)
    
    def dfs(self, s):
        visited = set()
        self.dfs_traversal(s, visited)

    def detect_cycle_traversal(self, s, visited):
        if s in visited:
            self.cycle = True
            return 
        visited.add(s)
        if s in self.graph:
            for adj in self.graph[s]:
                self.detect_cycle_traversal(adj, visited)
    
    def detect_cycle(self):
        visited = set()
        for node in self.graph.keys():
            if node not in visited and not self.cycle:
                self.detect_cycle_traversal(node, visited)
                if self.cycle:
                    return self.cycle
        return self.cycle
