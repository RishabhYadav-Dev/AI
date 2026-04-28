# AIM: Program on uninformed search methods.
# TITLE: To write program on uninformed search methods using DFS and BFS methods.

# ##BFS## #<------
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # 👈 Queue 
    visited.add(start)

    while queue:
        node = queue.popleft()   # 👈 FIFO
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal:")
bfs(graph, 'A')

# ##DFS## #<------
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited) # 👈 Recursion (acts like stack)

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\n\nDFS Traversal:")
dfs(graph, 'A')

#Direct Output





# THEORY:
# Uninformed search is a class of general-purpose search algorithms which operates in brute force-
# way. Uninformed search algorithms do not have additional information about state or search space
# other than how to traverse the tree, so it is also called blind search.

# DFS:
# First, the search technique starts from the root node A and then goes to the branch where node B is
# present (lexicographical order). Then it goes to node D because of DFS, and from D, there is only
# one node to traverse, i.e., node H. But after node H does not have any child nodes, we retrace the
# path in which we traversed earlier and again reach node B, but this time, we traverse through in the
# untraced path a traverse through node E. There are two branches at node E, but let’s traverse node I
# (lexicographical order) and then retrace the path as we have no further number of nodes after E to
# traverse. Then we traverse node J as it is the untraced branch and then again find we are at the end
# and retrace the path and reach node B and then we will traverse the untraced branch, i.e., through
# node C, and repeat the same process. This is called the DFS Algorithm.

# BFS:
# It starts from the root node A and then traverses node B. Till this step, it is the same as DFS. But
# here, instead of expanding the children of B as in the case of DFS, we expand the other child of A,
# i.e., node C because of BFS, and then move to the next level and traverse from D to G and then
# from H to K in this typical example. To traverse here, we have only taken into consideration the
# lexicographical order. This is how the BFS Algorithm is implemented.

# Conclusion: We understood the concept of uninformed search methods. Hence we implemented the
# BFS and DFS using Python.
