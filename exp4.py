#code
import heapq

def a_star(graph, start, goal, h):
    pq = [(0, start)]   # priority queue
    g = {start: 0}      # cost from start
    parent = {}

    while pq:
        f, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            return path[::-1], g[goal]

        for neigh, cost in graph[node]:
            new_cost = g[node] + cost

            if neigh not in g or new_cost < g[neigh]:
                g[neigh] = new_cost
                heapq.heappush(pq, (new_cost + h[neigh], neigh))
                parent[neigh] = node

    return None, None


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [],
    'F': [('H', 4)],
    'H': [('J', 7)],
    'J': []
}

# Heuristic
h = {
    'A': 16, 'B': 14, 'C': 4,
    'D': 6, 'E': 5, 'F': 7,
    'H': 3, 'J': 0
}

path, cost = a_star(graph, 'A', 'J', h)
print("Path:", path)
print("Cost:", cost)






# Output
# Path: ['A', 'C', 'F', 'H', 'J']
# Cost: 16


# AIM: Program on informed search methods.
# TITLE: To implement a Star search method program in python.

# Informed search algorithms are a type of search algorithm that uses heuristic functions to guide the
# search process. For example, a heuristic function calculates the cost of moving from a starting state
# to a goal state. By employing this assessment, informed search algorithms can select search paths
# more likely to lead to the desired state.
# A* search, iterative deepening A*, and best first search in artificial intelligence are examples of
# informed search algorithms. These algorithms are frequently employed in AI applications and have
# successfully resolved challenging issues.
# A* Search Algorithm
# To determine the best route from the starting node to the goal node, the A* Search Algorithm
# combines the cost function and the heuristic function.  f(n)=g(n)+h(n), where g(n) is the cost from
# the starting node to node n and h(n) is the anticipated cost from node n to the goal node, expands
# the one with the lowest overall cost.

# Steps of A* Search Algorithm:

# 1. Set the starting node&#39;s g-value to 0 and its h-value to the expected cost of getting there from
# the starting node.
# 2. Expand the node with the lowest total f(n) cost.
# 3. Stop the search and return the route from the starting node to the goal node if the expanded
# node is the desired node.
# 4. If not, determine the g-value and h-value, and update the f-value for each neighbor of the
# expanded node. Finally, add the neighbor to the open list if it&#39;s not already there.
# 5. Until the goal node is located or the open list is empty, repeat steps 2-4.
# In this example, we will traverse the given graph using the A* algorithm. The heuristic value of all
# states is given in the table so we will calculate the f(n) of each state using the formula
# f(n)=g(n)+h(n), where g(n) is the cost to reach any node from the start state.
