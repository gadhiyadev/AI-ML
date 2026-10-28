import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    row, col = position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
            neighbors.append((r, c))

    return neighbors

def astar_algorithm(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    start_node.g = 0
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node == goal_node:
            path = []
            curr = current_node
            while curr:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]   

        for neighbor_pos in get_neighbors(current_node.position, grid):
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, goal)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(node.position == neighbor_node.position and node.f <= neighbor_node.f for node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    print("\n--- A* Search Algorithm ---\n")
    print(f"Start: {start} | Goal: {goal}\n")

    path = astar_algorithm(grid, start, goal)

    if path:
        print("Path found successfully:")
        print(" -> ".join(str(pos) for pos in path))
        print(f"\nTotal steps: {len(path) - 1}\n")
    else:
        print("No path found to the goal.")
