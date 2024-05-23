import time

class DFS:

    def __init__(self, maze=None):
        self.maze = maze
        self.goal = (1,1)
        self.directions = 'ESWN'

    def solve(self):
        start_time = time.time()
        start = (self.maze.rows, self.maze.cols)
        visited = set([start])
        stack = [start]
        path = {}
        while stack:
            cur = stack.pop()
            if cur == self.goal:
                break
            for d in self.directions:
                if self.maze.maze_map[cur][d]:
                    if d == 'E':
                        next_node = (cur[0], cur[1] + 1)
                    elif d == 'S':
                        next_node = (cur[0] + 1, cur[1])
                    elif d == 'W':
                        next_node = (cur[0], cur[1] - 1)
                    elif d == 'N':
                        next_node = (cur[0] - 1, cur[1])
                    if next_node in visited:
                        continue
                    visited.add(next_node)
                    stack.append(next_node)
                    path[next_node] = cur
        dfs_path = {}
        cur = self.goal
        while cur != start:
            dfs_path[path[cur]] = cur
            cur = path[cur]
        end_time = time.time()
        return dfs_path, visited, end_time - start_time
