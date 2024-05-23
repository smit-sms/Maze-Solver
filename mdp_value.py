import random, time
from mdp import MDP

class MDP_value(MDP):

    def __init__(self, maze=None):
        super().__init__(maze)

        self.target = [self.goal]
        self.values = {state: 0 for state in self.actions.keys()}
        self.values[self.target[0]] = 1
        self._reward = -4  # LIVING REWARD
        self._max_error = 10 ** (-3)
        self.algoPath = {}
        self.explored = []
        self.mainTime = 0
        self.directions = 'ESWN'

    def solve(self):
        start = time.time()
        while True:
            delta = 0
            for state in self.actions.keys():
                if state == self.target[0]:
                    continue
                    
                utilityMax = float('-infinity')
                for action, prob in self.actions[state].items():
                    for direction in action:
                        if self.maze.maze_map[state][direction]:
                            childCell = self.move(state, direction)
                    reward = self._reward
                    if childCell == self.target[0]:
                        reward = 10000         # Reward for reaching the target
                    utility = 0
                    utility += super().calculate_ValueIterationUtility(prob, reward, childCell, self.values)

                    if utility > utilityMax:
                        utilityMax = utility

                delta = max(delta, abs(utilityMax - self.values[state]))
                self.values[state] = utilityMax
            if delta < self._max_error:
                break

        node = (self.maze.rows, self.maze.cols)
        while True:
            selectedNode = None
            selectedNodeVal = None
            if node == self.target[0]:
                break

            for direction in self.directions:
                if self.maze.maze_map[node][direction] and self.move(node, direction) not in self.explored:
                    traverseDirection = self.move(node, direction)
                    if traverseDirection == self.target[0]:
                        selectedNode = traverseDirection
                        break
                    if selectedNodeVal is None:
                        selectedNode = traverseDirection
                        selectedNodeVal = self.values[selectedNode]
                    else:
                        tempNode = traverseDirection
                        if selectedNodeVal < self.values[tempNode]:
                            selectedNode = tempNode
                            selectedNodeVal = self.values[tempNode]

            self.explored.append(node)
            self.algoPath[node] = selectedNode
            node = selectedNode
        end = time.time()
        self.mainTime = end-start
        return self.algoPath, self.explored, self.mainTime
