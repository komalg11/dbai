class AStarGraph(object):
    def __init__(self):
        self.barriers = []  # List to hold the barrier coordinates
        t = int(input("Enter total number of barriers: "))
        for i in range(t):
            # Collecting the coordinates for each barrier
            x = int(input(f"Enter row number for barrier point {i+1}: "))
            y = int(input(f"Enter column number for barrier point {i+1}: "))
            self.barriers.append((x, y))

    def heuristic(self, start, goal):
        # Heuristic function to estimate the cost from start to goal
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def get_vertex_neighbours(self, pos):
        # Get the valid neighbouring positions from the current position
        n = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 5 or y2 < 0 or y2 > 5:
                continue  # Skip out-of-bounds positions
            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        # Return the movement cost from position a to position b
        if b in self.barriers:
            return 100  # High cost for barriers
        return 1  # Normal cost for free space

def AStarSearch(start, end, graph):
    G = {}  # Actual movement cost to each position from the start position
    F = {}  # Estimated movement cost from start to end going through the position

    G[start] = 0  # Cost from start to start is zero
    F[start] = graph.heuristic(start, end)  # Initial estimated cost

    closedVertices = set()  # Set of evaluated positions
    openVertices = set([start])  # Set of positions to be evaluated
    cameFrom = {}  # Map of navigated positions

    while len(openVertices) > 0:
        current = None
        currentFscore = None
        for pos in openVertices:
            # Find the position with the lowest F score
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if current == end:
            # If the goal is reached, reconstruct the path
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[end]

        openVertices.remove(current)
        closedVertices.add(current)

        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue  # Ignore already evaluated neighbours
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue  # This is not a better path

            # Record the best path to the neighbour
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    raise RuntimeError("A* failed to find a solution")

if __name__ == "__main__":
    graph = AStarGraph()
    s1 = int(input("Enter row number for start point: "))
    s2 = int(input("Enter column number for start point: "))
    g1 = int(input("Enter row number for goal point: "))
    g2 = int(input("Enter column number for goal point: "))
    result, cost = AStarSearch((s1, s2), (g1, g2), graph)
    print("Route:", result)
    print("Cost:", cost)




'''
1.Create a graph that can hold barrier locations (obstacles).
2.Ask the user how many barriers there are, then collect the coordinates of each barrier and store them.
3.Use a heuristic function to estimate the cost to reach the goal from any position. This estimation is based on the distance between two points.
4.Define possible moves (up, down, left, right, diagonal) for each position on the grid.
5.Check each move to ensure it stays within the grid’s boundaries. If valid, add it to a list of neighboring positions.
6.Assign a high cost to move into a barrier and a regular cost to move into a free space.
7.Initialize costs for reaching positions, starting with zero cost to reach the start position.
8.Track positions to explore, starting with the start position, and mark explored positions.
9.While there are positions to explore:
    Pick the position with the lowest estimated cost.
    If it’s the goal, reconstruct the path taken and return it with the final cost.
    If not, remove the position from the list to explore and add it to the explored list.
    For each neighboring position:
        Skip it if already explored.
        Calculate the cost to move to this neighbor from the current position.
        If this cost is better than previously recorded, update the path and cost records for this neighbor.
10.Get start and goal coordinates from the user.
11.Run the A* algorithm to find the path from start to goal.
12.Print the path found and the total cost.
'''
