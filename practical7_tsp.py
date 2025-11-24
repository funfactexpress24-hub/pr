from itertools import permutations

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

def traveling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(vertices):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = (start,) + perm + (start,)

    return min_path, min_cost

start = 'A'
path, cost = traveling_salesman(graph, start)
print(f"Optimal Path: {path}\nMinimum Cost: {cost}")
