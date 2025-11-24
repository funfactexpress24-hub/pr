import heapq

goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state_flat = sum(goal_state, [])

class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        h = 0
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:
                    goal_x, goal_y = divmod(goal_state_flat.index(val), 3)
                    h += abs(goal_x - i) + abs(goal_y - j)
        return h

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(state):
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def a_star(start_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, Node(start_state))

    while open_list:
        node = heapq.heappop(open_list)
        if node.state == goal_state:
            return reconstruct_path(node)
        closed_set.add(tuple(map(tuple, node.state)))
        for neighbor in get_neighbors(node.state):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue
            heapq.heappush(open_list, Node(neighbor, node, node.g + 1))
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

start_state = [[0, 8, 1], [2, 4, 3], [7, 6, 5]]
path = a_star(start_state)
for step in path:
    for row in step:
        print(row)
    print()
