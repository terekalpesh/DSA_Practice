# Detect a cycle in an undirected graph.

def dfs(v, graph, visited, parent):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, v):
                return True
        elif parent != neighbor:
            return True
    
    return False

def detect_cycle(graph, num_vertices):
    visited = [False] * num_vertices

    for v in range(num_vertices):
        if not visited[v]:
            if dfs(v, graph, visited, -1):
                return True
    return False

# Graph cycle (0-1-2)
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

vertices = 3

if detect_cycle(graph, 3):
    print('Cycle detected.')
else:
    print('No cycle detected.')