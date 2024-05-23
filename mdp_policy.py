import random, time
from mdp import MDP

class MDP_policy(MDP):
    def __init__(self, maze=None):
        super().__init__(maze)

        self.target = [self.goal]
        self.values = {state: 0 for state in self.actions.keys()}
        self.values[self.target[0]] = pow(10, 7)
        self.policyValues = {s: random.choice('N') for s in self.actions.keys()}
        self._reward = {state: -40 for state in self.actions.keys()}  # LIVING REWARD
        self._reward[self.target[0]] = pow(10, 8)   # Reward for reaching the target
        self.algoPath = {}
        self.mainTime = 0
        self.explored = set()

    def solve(self):
        start = time.time()
        policyTrigger = True
        while policyTrigger:
            policyTrigger = False
            valueTrigger = True

            while valueTrigger:
                valueTrigger = False
                for state in self.actions.keys():
                    self.explored.add(state)
                    if state == self.target[0]:
                        continue

                    utilityMax = float('-infinity')
                    actionMax = None
                    for action, prob in self.actions[state].items():
                        for direction in action:
                            if self.maze.maze_map[state][direction]:
                                childNode = self.move(state, direction)

                        utility = super().calculate_PolicyIterationUtility(prob, self._reward, state, childNode, self.values)

                        if utility > utilityMax:
                            utilityMax = utility
                            actionMax = action

                        self.policyValues[state] = actionMax
                        self.values[state] = utilityMax

                        if self.policyValues[state] != actionMax:
                            policyTrigger = True
                            self.policyValues[state] = actionMax

        node = (self.maze.rows, self.maze.cols)
        while node != self.target[0]:
            nextNode = self.move(node, self.policyValues[node])
            self.algoPath[node] = nextNode
            node = nextNode

        end = time.time()
        return self.algoPath, self.explored, end - start
