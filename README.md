# 8-Puzzle Solver: A* vs. Greedy Best-First Search

An artificial intelligence implementation solving the classic 8-Puzzle game using Informed Search Strategies in Python.

## 🧠 Heuristics Explained

To evaluate the states, this project focuses on two distinct informed metrics:

1. **Misplaced Tiles ($h_1$):** Counts the absolute number of tiles that are out of their correct final positions. While simple, it is a weaker heuristic because it doesn't account for *how far* a tile needs to move.
2. **Manhattan Distance ($h_2$):** Computes the sum of absolute horizontal and vertical distances of each tile from its target coordinates. This is the **primary heuristic** used in this project's code because it is highly informed, admissible, and consistent.

### The Algorithm Formulae
* **Greedy Best-First Search:** Evaluates paths purely using future heuristic estimations:
  $$f(n) = h(n)$$
* **A\* Search:** Achieves absolute optimality by balancing the path cost already traveled with the estimated future distance:
  $$f(n) = g(n) + h(n)$$

---

## 🚀 How to Set Up and Run

### 1. Clone the repository
```bash
git clone [https://github.com/WhiteGhost-001/8-Tile-Problem.git](https://github.com/WhiteGhost-001/8-Tile-Problem.git)
cd 8-Tile-Problem
