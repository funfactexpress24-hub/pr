graph = {
    'a': ['b', 'c', 'd'],
    'b': ['e', 'f'],
    'c': ['g'],
    'd': [],
    'e': [],
    'f': [],
    'g': []
}

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            if result:
                return result
    return None

start_node, goal_node = 'a', 'e'
path = dfs(graph, start_node, goal_node)
print(f"Path found from {start_node} to {goal_node}: {path}")
