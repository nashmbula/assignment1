# Minimax Hand-Trace: Cafeteria subtree

Game: CampusMind Challenge. Start = Main Gate, 3 plies, MAX moves first.
utility(loc) = hop_distance(loc, Library) - hop_distance(loc, Cafeteria)

## Tree (MAX has moved to Cafeteria)

Ply 1: MAX moved Main Gate -> Cafeteria
Ply 2: MIN chooses from: StudentAffairs, MainGate
Ply 3: MAX chooses from the neighbours of each MIN choice

```
Cafeteria (MIN to move)            backed-up value = 3
├── MIN goes to StudentAffairs     MAX picks max(3, 0) = 3
│   ├── Cafeteria   utility = 3
│   └── ScienceLab  utility = 0
└── MIN goes to MainGate           MAX picks max(-1, 3) = 3
    ├── Admin       utility = -1
    └── Cafeteria   utility = 3
```

## Terminal utilities

| Terminal   | hop_distance to Library | hop_distance to Cafeteria | utility |
|------------|-------------------------|---------------------------|---------|
| Cafeteria  | 3                       | 0                         | 3       |
| ScienceLab | 2                       | 2                         | 0       |
| Admin      | 1                       | 2                         | -1      |
| Cafeteria  | 3                       | 0                         | 3       |

## Backing up the values

1. MAX level (ply 3): under StudentAffairs the larger of 3 and 0 is 3. Under MainGate the larger of -1 and 3 is 3.
2. MIN level (ply 2): min(3, 3) = 3.
3. So Main Gate -> Cafeteria is worth 3.
4. Main Gate -> Admin is worth -1 (MIN answers Library, and MAX is forced back to Admin, utility -1). MAX picks Cafeteria.

## Alpha-beta note

Neighbours are tried in the order Admin: Library, ScienceLab, MainGate.
Admin subtree: MIN tries Library first, MAX's only move is Admin (-1), so beta = -1.
Next, under ScienceLab, MAX sees Admin (-1), so alpha = -1. Now alpha = -1 and
beta = -1, so beta <= alpha and StudentAffairs is pruned (it could only raise the
value, and MIN will never allow that). The same happens under MainGate:
Cafeteria is pruned. Two leaves are skipped.

Leaves evaluated: minimax = 9, alpha-beta = 7.

## Extension: MIN moves first

- New game value: -1
- MIN's best first move: Admin, with value -1 (Cafeteria is worth 0)

Why it changed: the recursion now alternates MIN, MAX, MIN instead of
MAX, MIN, MAX. The player who makes the last move (ply 3) picks straight from
the leaf utilities. Before, that was MAX, who could step onto Cafeteria (3)
from MainGate or StudentAffairs. Now it is MIN, who takes the lowest leaf
available. From Admin, every ply-2 position (MainGate, ScienceLab, Library) has
Admin (-1) as a neighbour, so MIN can always reach -1 and MAX cannot avoid it.
Cafeteria is worth 0 rather than 3 for the same reason: from StudentAffairs,
MIN picks ScienceLab (0) instead of letting MAX take Cafeteria (3). The value
fell from 3 to -1 because the last choice moved from the maximiser to the minimiser.