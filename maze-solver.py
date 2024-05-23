import argparse
from pyamaze import maze, agent, textLabel, COLOR
from dfs import DFS
from bfs import BFS
from astar import A_STAR
from mdp_value import MDP_value
from mdp_policy import MDP_policy
import tracemalloc as memory_trace

algo_map = {
    'DFS': DFS,
    'BFS': BFS,
    'A*': A_STAR,
    'MDP_value': MDP_value,
    'MDP_policy': MDP_policy
}

def start_memory_tracing():
    memory_trace.stop()
    memory_trace.start()
    
def stop_memory_tracing(): 
    memory_size, memory_peak = memory_trace.get_traced_memory()
    return memory_size, memory_peak

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', help='If new maze is to be generated or not? True/False', type=str)
    parser.add_argument('--maze-size', help='Size of the maze to be generated/loaded. Existing mazes: 10, 25, 50, 100', type=int)
    parser.add_argument('--algorithm', help='Algorithm to be run on the maze', type=str)
    parser.add_argument('--manhattan', help='Use Manhattan distance for A* Algorithm? True/False', type=str)
    args = parser.parse_args()

    if args.generate is None:
        print("Please specify if the new maze is to be generated or not?")
        exit(1)

    if args.maze_size is None:
        print("Please specify the maze size to generate. Existing mazes: 10, 25, 50, 100")
        exit(1)

    if args.algorithm is None:
        print("Please specify the algorithm to run.")
        exit(1)

    generate = True if args.generate in ('True','true') else False
    maze_size = args.maze_size
    algorithm = args.algorithm

    if generate:
        load_maze = None
    else:
        load_maze = f'./mazes/maze-{maze_size}.csv'

    m = maze(maze_size, maze_size)
    m.CreateMaze(loopPercent=100, theme=COLOR.light, loadMaze=load_maze, saveMaze=generate)

    if algorithm == 'A*':
        if args.manhattan is None:
            print("Please specify whether to use manhattan distance or euclidean distance using the flag '--manhattan True/False'?")
            exit(1)
        manhattan = True if args.manhattan in ('True','true') else False
        operation = algo_map[algorithm](m, manhattan)
    else:
        operation = algo_map[algorithm](m)

    start_memory_tracing()

    final_path, explored_path, spent_time = operation.solve()

    memory_size, memory_peak = stop_memory_tracing()
    memory_consumed = round((memory_peak/(1024*1024)), 3)

    path_agent = agent(m, footprints=True, filled=True)
    m.tracePath({path_agent: final_path}, delay=10)

    explored_agent = agent(m, goal=(1,1), footprints=True, filled=False, color=COLOR.red)
    for i in range(len(explored_path)):
        explored_agent.position = list(explored_path)[i]
    m.tracePath({explored_agent: explored_path}, delay=10)

    textLabel(m, 'Algorithm', algorithm)
    textLabel(m, 'Length of Shortest Path', len(final_path) + 1)
    textLabel(m, 'Time spent to find the path (in seconds)', spent_time)
    textLabel(m, 'Memory Consumed for the algorithm (in MB)', memory_consumed)
    print(f'Time taken to run {algorithm}: {spent_time}')
    m.run()

if __name__ == '__main__':
    main()
