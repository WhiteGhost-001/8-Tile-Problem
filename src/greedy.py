import heapq
from utils import get_neighbors, get_manhattan_distance, print_board, GOAL

def greedy_search(start_state):
    pq = []
    initial_h = get_manhattan_distance(start_state)
    heapq.heappush(pq, (initial_h, start_state, []))
    
    visited = set()
    nodes_expanded = 0
    
    while pq:
        h, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1
        
        if current == GOAL:
            return path + [current], nodes_expanded
            
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_h = get_manhattan_distance(neighbor)
                heapq.heappush(pq, (new_h, neighbor, path + [current]))
                
    return None, nodes_expanded

if __name__ == "__main__":
    start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    
    print("Initial State:")
    print_board(start)
    
    path, nodes = greedy_search(start)
    print(f"--- Greedy Search Results ---")
    print(f"Nodes Expanded: {nodes}")
    print(f"Total Steps to Solve: {len(path) - 1}\n")
