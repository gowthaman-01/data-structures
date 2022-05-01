class Graph:
    def __init__(self):
        self.graph = {}
        self.cycle = False
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def dfs_traversal(self, s, visited):
        if s in visited:
            return 
        visited.add(s)
        print(s)
        if s in self.graph:
            for a in self.graph[s]:
                self.dfs_traversal(a, visited)

    def dfs(self, s):
        self.visited = set()
        self.dfs_traversal(s, self.visited)

    def detect_cycle_traversal(self, node, visited):
        if node in visited:
            self.cycle = True
            return 
        else:
            visited.add(node)
            if node in self.graph:
                for adj in self.graph[node]:
                    if adj != self.prev:
                        self.prev = node
                        self.detect_cycle_traversal(adj, visited)

    def detect_cycle(self):
        if self.cycle:
            return self.cycle
        self.prev = None
        for node in self.graph.keys():
            self.visited = set()
            self.detect_cycle_traversal(node, self.visited)
            if self.cycle:
                return self.cycle
        return self.cycle
            