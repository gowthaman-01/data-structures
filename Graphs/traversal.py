from collections import deque
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

# Recursive dfs


def recursiveDfs(graph, start, traverse, visited):
    traverse.append(start)
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            recursiveDfs(graph, node, traverse, visited)

# Iterative dfs


def iterativeDfs(graph, start):
    visited = set()
    stack, traverse = [], []
    stack.append(start)
    while stack:
        top = stack.pop()
        traverse.append(top)
        visited.add(top)
        for node in graph[top]:
            if node not in visited:
                stack.append(node)
    return traverse

# Bfs


def bfs(graph, start):
    q, visited, traverse = deque([]), set(), []
    q.append(start)
    while q:
        top = q.popleft()
        visited.add(top)
        traverse.append(top)
        for node in graph[top]:
            if node not in visited:
                q.append(node)
    return traverse


print(bfs(graph, 'a'))
