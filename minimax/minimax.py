from campusmind import *

leaves = 0

def minimax(loc, depth, is_max):
    global leaves
    if is_terminal(depth):
        leaves += 1
        return utility(loc)
    values = [minimax(n, depth + 1, not is_max) for n in GRAPH[loc]]
    return max(values) if is_max else min(values)

if __name__ == "__main__":
    print("Game value:", minimax(START, 0, True))
    print("Terminal states evaluated:", leaves)
    for child in GRAPH[START]:
        print(f"  MAX plays {child}: {minimax(child, 1, False)}")