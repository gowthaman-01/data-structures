graph = {
    '1': ['0'],
    '3': ['1'],
    '2': ['1'],
    '4': [],
    '5': ['4', '2'],
    '6': ['4', '3'],
    '7': ['5', '6'],
    '0': []
}


def dfsCycle(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            if dfsCycle(graph, neighbour, visited):
                return True
        visited.remove(node)
    else:
        return True


def detectCycle(graph):
    explored = set()
    for node in graph.keys():
        if node not in explored:
            explored.add(node)
            visited = set()
            if dfsCycle(graph, node, visited):
                return True
    return False


def dfs(graph, node, visited, sorted):
    if node not in visited:
        sorted = []
        visited.add(node)
        for neighbour in graph[node]:
            sorted = dfs(graph, neighbour, visited, sorted) + sorted
        return [node] + sorted
    else:
        return []


def topoSort(graph):
    sorted = []
    if detectCycle(graph):
        return "Graph contains a cycle"
    visited = set()
    for node in graph:
        if node not in visited:
            sorted = dfs(graph, node, visited, sorted) + sorted
    return sorted


print(topoSort(graph))
