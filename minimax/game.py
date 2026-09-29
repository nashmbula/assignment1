from collections import deque
graph={
    "MainGate":  ["Admin", "Cafeteria"],
    "Admin":     [],   
    "Cafeteria": [],  
    "Library":   [],   

}

START = "MainGate"
PLIES = 3

def hop_distance(a, b):
    """Fewest edges between two locations (BFS)."""
    seen, queue = {a}, deque([(a, 0)])
    while queue:
        node, d = queue.popleft()
        if node == b:
            return d
        for n in GRAPH[node]:
            if n not in seen:
                seen.add(n)
                queue.append((n, d + 1))
    raise ValueError(f"{b} not reachable from {a}")

def utility(location):
    return hop_distance(location, "Library") - hop_distance(location, "Cafeteria")

def is_terminal(depth):
    return depth == PLIES