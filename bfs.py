import time

class BFS:

    def __init__(self, maze=None):
        self.maze = maze
        self.goal = (1,1)
        self.directions = 'ESWN'

    def solve(self):
        start_time = time.time()
        start = (self.maze.rows, self.maze.cols)
        vis = [start]
        queue = [start]
        path = {}
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur == self.goal:
                break
            for d in self.directions:
                if self.maze.maze_map[cur][d]:
                    if d == 'E':
                        Next = (cur[0], cur[1] + 1)
                    elif d == 'S':
                        Next = (cur[0] + 1, cur[1])
                    elif d == 'W':
                        Next = (cur[0], cur[1] - 1)
                    elif d == 'N':
                        Next = (cur[0] - 1, cur[1])
                    if Next in vis:
                        continue
                    vis.append(Next)
                    queue.append(Next)
                    path[Next] = cur
        bfs_path = {}
        cur = (1, 1)
        while cur != start:
            bfs_path[path[cur]] = cur
            cur = path[cur]
        end_time = time.time()
        return bfs_path, vis, end_time - start_time
