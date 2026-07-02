GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_manhattan_distance(state):
    """
    Heuristic 1: Manhattan Distance
    Calculates the sum of absolute vertical and horizontal distances 
    of tiles from their goal positions.
    """
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            r, c = divmod(i, 3)
            goal_idx = GOAL.index(tile)
            gr, gc = divmod(goal_idx, 3)
            distance += abs(r - gr) + abs(c - gc)
    return distance

def get_misplaced_tiles(state):
    """
    Heuristic 2: Misplaced Tiles
    Counts how many tiles are currently not in their correct goal positions.
    """
    count = 0
    for i, tile in enumerate(state):
        if tile != 0 and tile != GOAL[i]:
            count += 1
    return count

def get_neighbors(state):
    """Generates valid next states by shifting the empty space (0)."""
    neighbors = []
    idx = state.index(0)
    r, c = divmod(idx, 3)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            neighbor_idx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def print_board(state):
    """Helper to cleanly print the 3x3 grid layout."""
    for i in range(0, 9, 3):
        print(f"[ {state[i]} {state[i+1]} {state[i+2]} ]")
    print()
