import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2)],
    'B': [('D', 5)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {'S': 7, 'A': 6, 'B': 5, 'C': 2, 'D': 1, 'G': 0}

def best_first_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], start, [start]))
    visited = set()

    while pq:
        (h, node, path) = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for (neighbor, _) in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

start, goal = 'S', 'G'
path = best_first_search(graph, start, goal)
print(f"Best-First path from {start} to {goal}: {path}")
