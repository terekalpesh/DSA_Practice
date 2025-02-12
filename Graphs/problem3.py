# Find the shortest path between two nodes in an unweighted graph using BFS.

from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])

    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'

path = bfs_shortest_path(graph, start_node, end_node)
print(f'Shortest path from {start_node} to {end_node}: {path}')