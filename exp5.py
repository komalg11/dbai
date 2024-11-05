# Selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current element is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the min_index if a smaller element is found
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element with the first element
    return arr

# Take input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# Prim's

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst, total_weight = [], 0
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = [tuple(map(int, input("Enter edge (u, v, weight): ").strip().split())) for _ in range(m)]
mst, total_weight = kruskal(n, edges)

print("\nEdges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u}-{v} (weight: {w})")
print(f"\nTotal weight of MST: {total_weight}")


'''
Selection Sort
1.Start with the first item in the list.
2.Look through the rest of the list to find the smallest item.
3.Swap this smallest item with the first item.
4.Move to the next item in the list and repeat the process of finding the smallest item in the remaining list and swapping it.
5.Keep repeating until all items are in order.

Kruskal’s Algorithm for Minimum Spanning Tree (MST)
1.Sort all edges by their weight from smallest to largest.
2.Start with an empty set of edges for the MST.
3.For each edge in the sorted list:
    Check if adding this edge will form a cycle (using a helper that tracks connections between nodes).
    If it doesn’t form a cycle, add this edge to the MST.
4.Repeat until you’ve included enough edges to connect all nodes.
5.The final set of edges forms the MST, and their total weight is the minimum required to connect all nodes.
'''
