from campusmind import *
from minimax import minimax

print("MIN moves first")
print("Game value:", minimax(START, 0, False))
for child in GRAPH[START]:
    print(f"  MIN plays {child}: {minimax(child, 1, True)}")