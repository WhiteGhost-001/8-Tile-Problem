import heapq
from utils import get_neighbors, get_manhattan_distance, print_board, GOAL

def a_star_search(start_state):
    pq = []
    initial_h = get_manhattan_distance(start_state)
    heapq.heappush(pq, (initial_h, 0, start_state, []))
    
    visited = set()
    nodes_expanded = 0
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1
        
        if current == GOAL:
            return path + [current], nodes_expanded
            
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_h = get_manhattan_distance(neighbor)
                new_f = new_g + new_h
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [current]))
                
    return None, nodes_expanded

if __name__ == "__main__":
    start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    
    print("Initial State:")
    print_board(start)
    
    path, nodes = a_star_search(start)
    print(f"--- A* Search Results ---")
    print(f"Nodes Expanded: {nodes}")
    print(f"Total Steps to Solve: {len(path) - 1}\n")
