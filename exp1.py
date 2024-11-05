# DFS for an undirected graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from node A:")
dfs(graph, 'A')

# bfs

from collections import deque

# BFS for an undirected graph
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nBFS traversal starting from node A:")
bfs(graph, 'A')


'''
Depth-First Search (DFS) Algorithm (Simple Language)
1.Start with a starting node (like "A") and mark it as visited.
2.Print or record the current node.
3.For each neighbor (connected node) of the current node:
      If the neighbor hasn’t been visited, repeat these steps starting from that neighbor.
4.Continue this process until all reachable nodes have been visited.

Breadth-First Search (BFS) Algorithm (Simple Language)
1.Start with a starting node (like "A") and mark it as visited.
2.Add this node to a queue (a list where nodes are processed in order).
3.While there are nodes in the queue:
    Take the first node from the queue, print or record it.
    For each neighbor of this node:
        If the neighbor hasn’t been visited, mark it as visited and add it to the queue.
4.Continue this until the queue is empty (all reachable nodes have been visited).
'''

