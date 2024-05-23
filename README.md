# Maze Solver - Search and MDP Algorithms

## Overview
This project is designed to explore and compare various search and Markov Decision Process (MDP) algorithms for solving mazes. The maze solver implements Depth First Search (DFS), Breadth First Search (BFS), A-Star (A*) algorithms using both Euclidean and Manhattan heuristics, as well as MDP algorithms including Value Iteration and Policy Iteration. Each algorithm is evaluated on mazes of different sizes, generated using the Pyamaze package, to assess their performance based on metrics such as the time taken to find the path, the number of steps to reach the goal, and memory consumption.

The project aims to provide a comprehensive analysis of how different search and decision-making strategies perform in navigating through complex environments. It highlights the strengths and weaknesses of each algorithm in terms of speed, efficiency, and resource utilization. By comparing these algorithms, the project offers insights into their practical applications and suitability for different types of problems in the field of artificial intelligence and robotics.

**Key Features:**
1. Maze Generation: Utilizes the Pyamaze package to create customizable mazes of various sizes and complexities.
2. Algorithm Implementation: Implements classic search algorithms (DFS, BFS, A*) and MDP algorithms (Value Iteration, Policy Iteration) to solve the generated mazes.
3. Performance Metrics: Evaluates algorithms based on time taken to find the path, the number of steps to the goal, and memory usage.
4. Comparative Analysis: Provides detailed comparisons and visualizations of the performance of each algorithm, helping to understand their practical implications.
5. User Interaction: Allows users to specify maze size, algorithm type, and other parameters through command-line arguments for flexible experimentation.

**Algorithms Implemented:**
1. Depth First Search (DFS)
2. Breadth First Search (BFS)
3. A-Star Algorithm (A)*
    - Euclidean Distance
    - Manhattan Distance
4. Markov Decision Process (MDP)
    - Value Iteration
    - Policy Iteration
  
## Project Structure
- `maze-solver.py`: Main script to run the maze solver.
- `dfs.py`: DFS algorithm implementation.
- `bfs.py`: BFS algorithm implementation.
- `astar.py`: A-Star algorithm implementation.
- `mdp.py`: Base class for MDP algorithms.
- `mdp_value.py`: MDP Value Iteration algorithm implementation.
- `mdp_policy.py`: MDP Policy Iteration algorithm implementation.

## Prerequisites
- Python 3.9 and above
- Pyamaze
    ```
    pip install pyamaze
    ```

## Running the Project
To run the maze solver on a saved maze of size 25x25 using the DFS algorithm, use the following command:
```
cd <directory>
python maze-solver.py --generate False --maze-size 25 --algorithm DFS
```

**Command Line Arguments**
- `--generate`: Specifies whether a new maze should be generated. Accepts True or False.
- `--maze-size`: Specifies the size of the maze. Accepts values like 10, 25, 50, 100.
- `--algorithm`: Specifies the algorithm to be used. Options include 'DFS', 'BFS', 'A*', 'MDP_value', and 'MDP_policy'.
- `--manhattan`: Specifies whether to use Manhattan distance for the A* algorithm. Accepts True or False.

## NOTE
> IF 'generate' is True, then the maze will be saved in the current directory. To run another algorithm on the new maze, kindly save this newly generated maze in the '/mazes' directory as 'maze-{name_of_maze_to_save}'. 

  Now, the updated run command would be as follows:
  ```
  python .\maze-solver.py --generate False --maze-size {name_of_maze_to_save} --algorithm DFS
  ```

> If in case the MDP algorithms fail to converge or take too much time, please increase the rewards in the script. The current state of the algorithms is designed to work optimally for mazes till the range of 50x50. The rewards can be changed from the independent scripts of value iteration and policy iteration from the following lines:
  ```
  mdp_value.py: Line 34
  mdp_policy.py: Line 30
  ```

## Some Screenshots
<p float="left" align="center">
  <img src="https://github.com/smit-sms/Maze-Solver/assets/52400400/7748dd4e-d1d2-4045-81a4-03e517d048d7" width="400" />
  <img src="https://github.com/smit-sms/Maze-Solver/assets/52400400/4cdcd9fb-d107-4f74-9ac3-04ef6c93f2e1" width="400" /> 
  <br/>BFS on 25x25 Maze &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; DFS on 25x25 Maze
</p>

## Example Commands
```
python maze-solver.py --generate False --maze-size 25 --algorithm DFS
```
```
python maze-solver.py --generate False --maze-size 25 --algorithm BFS
```
```
python maze-solver.py --generate False --maze-size 25 --algorithm A* --manhattan True
```
```
python maze-solver.py --generate False --maze-size 25 --algorithm A* --manhattan False
```
```
python maze-solver.py --generate False --maze-size 25 --algorithm MDP_value
```
```
python maze-solver.py --generate False --maze-size 25 --algorithm MDP_policy
```

