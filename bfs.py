from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = []
            self.graph[u].append(v)

    def bfs(self, s):
        q = deque()
        q.append(s)
        visited = set()
        while len(q):
            top = q.popleft()
            if top not in visited:
                print(top)
                visited.add(top)
                if top in self.graph:
                    for adj in self.graph[top]:
                        q.append(adj)
        
