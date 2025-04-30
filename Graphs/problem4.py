# Implement Dijkstra's algorithm to find the shortest path in a weighted graph.

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = None
        for node in unvisited_nodes:
            if current_node is None:
                current_node = node
            elif distances[node] < distances[current_node]:
                current_node = node

        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        unvisited_nodes.remove(current_node)

    return distances, previous_nodes

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

print(f'Shortest distance from {start_node}: {distances}')