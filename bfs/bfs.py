from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start_node, goal_node):
    if start_node == goal_node:
        return [start_node]
    
    queue = deque([[start_node]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                if neighbor == goal_node:
                    return new_path
                queue.append(new_path)
    return None

def dfs(graph, start_node, goal_node):
    stack = [[start_node]]
    visited = set()
    
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
    return None