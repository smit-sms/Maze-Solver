import time
import math
from queue import PriorityQueue

class A_STAR:

    def __init__(self, maze=None, isManhattan=True):
        self.maze = maze
        self.goal = (1,1)
        self.directions = 'ESWN'
        self.isManhattan = isManhattan

    def calculateEstimatedDistance(self, cur):
        if self.isManhattan:
            # MANHATTAN
            return abs(cur[0] - self.goal[0]) + abs(cur[1] - self.goal[1])

        # EUCLIDEAN
        return math.sqrt((cur[0] - self.goal[0]) ** 2 + (cur[1] - self.goal[1]) ** 2)

    def solve(self):
        start_time = time.time()
        start = (self.maze.rows, self.maze.cols)
        # The cost path from the start node to the current node
        g_score = {}
        # The cost path from the current node to goal node
        f_score = {}
        for cur in self.maze.grid:
            g_score[cur] = float('inf')
        for cur in self.maze.grid:
            f_score[cur] = float('inf')
        g_score[start] = 0
        f_score[start] = self.calculateEstimatedDistance(start)
        pq = PriorityQueue()
        pq.put((self.calculateEstimatedDistance(start), self.calculateEstimatedDistance(start), start))
        path = {}
        while not pq.empty():
            cur = pq.get()[2]
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
                    next_g = g_score[cur] + 1
                    next_f = next_g + self.calculateEstimatedDistance(Next)
                    if next_f < f_score[Next]:
                        g_score[Next] = next_g
                        f_score[Next] = next_f
                        pq.put((next_f, self.calculateEstimatedDistance(Next), Next))
                        path[Next] = cur
        astar_path = {}
        cur = self.goal
        while cur != start:
            astar_path[path[cur]] = cur
            cur = path[cur]
        end_time = time.time()
        return astar_path, path, end_time - start_time
