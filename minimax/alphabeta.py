import math
from campusmind import *

leaves = 0

def alphabeta(loc, depth, alpha, beta, is_max):
    global leaves
    if is_terminal(depth):
        leaves += 1
        return utility(loc)
    if is_max:
        best = -math.inf
        for n in GRAPH[loc]:
            best = max(best, alphabeta(n, depth + 1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    best = math.inf
    for n in GRAPH[loc]:
        best = min(best, alphabeta(n, depth + 1, alpha, beta, True))
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best

if __name__ == "__main__":
    print("Game value:", alphabeta(START, 0, -math.inf, math.inf, True))
    print("Terminal states evaluated:", leaves, "(full minimax: 9)")