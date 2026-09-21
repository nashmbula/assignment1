 week 1. Symbolic / Model-Based Design View

The symbolic or model-based view represents problems through explicit, programmed rules and formal search algorithms.
 The computer follows programmed rules and a search algorithm to calculate the shortest path between two locations. It examines the available roads, compares the distances between different points, and selects the route with the lowest total distance. This process continues systematically until the destination is reached.
 Road networks are modeled as explicit graph structures, where intersections act as nodes and road segments act as edges with static distance weights. Deterministic Logics  Algorithms such as A* or Dijkstra’s algorithm operate over these pre-defined graphs to compute guaranteed optimal paths based on fixed, rule-based constraints.



 Data-Driven / Learning-Based Design View

The data-driven or learning-based view relies on analyzing large volumes of historical and real-time data to adapt, predict, and dynamically adjust system behavior.

Core Mechanism: The system uses a lot of data to understand traffic patterns and estimate how long a journey will take. For example, Maps can collect information about how fast cars are moving on different roads. It can also look at past traffic information and the time of day. By comparing this information, it can predict whether a road is busy or clear and estimate the time it will take to reach the destination.
 Real-Time Data Streams:Ingests live speed, location updates, and sensor data from millions of active devices to detect dynamic delays as they happen.
Predictive Analytics: Machine learning models process historical traffic patterns alongside live data streams to dynamically update ETAs and optimize alternate routes.


week 3


 Assignment 2: Graph Search Exploration (BFS vs DFS)




 1. Exploration Strategies

a) Breadth-First Search (BFS)
 Strategy: Explores the graph  layer-by-layer. It visits all immediate neighbors of a node before moving deeper to the next depth level.
 Data Structure: Use s a Queue FIFO - First In, First Out  to keep track of nodes to expand.

b) Depth-First Search (DFS)
Strategy: Explores the graph path-by-path by going as deeply as possible along each branch before backtracking to explore alternate branches.
Data Structure:Uses a Stack LIFO - Last In, First Out or function call stack recursion.


 2. Theoretical Guarantees

Completeness Guaranteed Complete in finite graphs; always finds a solution if one exists. Not Guaranteed Can get trapped in infinite loops or deep branches.
 Optimality Guaranteed for unweighted graphs Always finds the shortest path in terms of steps. Not Guaranteed May find a longer path first based on exploration order. 






 4. Python Implementation (BFS & DFS)


 Graph representation using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

    
    if start_node == goal_node:
        return [start_node]
        
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal_node:
                    return new_path
    return None
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal_node:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return Non


week 4   

 Assignment 3: Informed Search & A* Algorithm





An uninformed search  like BFS or DFS explores nodes blindly based solely on structural connections. In contrast, an informed search uses a heuristic function $h(n)$**—an estimate of the cost from node $n$ to the goal.

Informed Exploration: The heuristic provides domain-specific guidance, steering the search towards the goal and drastically reducing the number of nodes evaluated.
Impact on Complexity: By focusing exploration along promising paths, heuristics reduce space and time complexity in practice compared to exhaustive brute-force searching.



 2. Why A* Stays Optimal

A* uses the evaluation function:
$$f(n) = g(n) + h(n)$$
$g(n)$: The exact cost incurred from the start node to node $n$.
$h(n)$: The estimated cost from node $n$ to the goal.

 Guarantees of Optimality:
1. Admissibility:** $h(n)$ must never overestimate the actual cost to reach the goal ($h(n) \le h^*(n)$). This ensures A* never overlooks a lower-cost route.
2. Consistency Monotonicity: For any node $n$ and neighbor $p$, $h(n) \le \text{cost}(n, p) + h(p)$. This prevents re-evaluating nodes and guarantees the first time a state is expanded, its path is optimal 

python implementation
import heapq

 Graph representation with edge weights (costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

 Straight-line distance heuristics h(n) to goal 'F'
heuristics = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

    
    visited = set()

    while open_set:
        f_score, current, path, g_score = heapq.heappop(open_set)

        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_g = g_score + weight
                new_f = new_g + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')
