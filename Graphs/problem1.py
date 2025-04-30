# Implement breadth-first search (BFS) and depth-first search (DFS) on a graph.

from collections import deque

# Breadth first search
def bfs(graph, start):
    visited = set()     # Keep track of visited nodes
    queue = deque([start])  # Queue for BFS

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Depth first search
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()


    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print('BFS traversal: ', end='')
bfs(graph, 0)
print('\n')

print('DFS traversal: ', end='')
dfs(graph, 0)
print()