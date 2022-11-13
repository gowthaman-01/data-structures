graph = {
    '4': ['2', '5', '6'],
    '5': ['6'], 
    '3': [],
    '6': [],
    '1': ['2', '4'],
    '2': ['3'],
    
    
}


def dfs(graph, node, visited, sorted):
    if node in visited: return 
    visited.add(node)
    for neighbour in graph[node]:
        dfs(graph, neighbour, visited, sorted)
    sorted.append(node)
    return sorted


def topoSort(graph):
    sorted = []
    visited = set()
    for node in graph:
        dfs(graph, node, visited, sorted)

    return sorted


print(topoSort(graph))
