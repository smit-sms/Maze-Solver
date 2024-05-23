import random, time

class MDP:
    def __init__(self, maze=None, isDeterministic=True):
        self.maze = maze
        self.goal = (1,1)
        self.actions = {}
        self._discount = 0.9
        self.isDeterministic = isDeterministic
        self.create_actions()

        self.target = [self.goal]

    def set_heuristics(self):
        for key, value in self.actions.items():
            for k, v in value.items():
                # NON DETERMINISTIC
                if k == 'N':
                    value[k] = 0.8
                elif k == 'W':
                    value[k] = 0.1
                elif k == 'E':
                    value[k] = 0.5
                elif k == 'S':
                    value[k] = 0.5

    def create_actions(self):
        # DETERMINISTIC
        for key, val in self.maze.maze_map.items():
            self.actions[key] = dict([(k, v) for k, v in val.items() if v == 1])

        # CHANGE TO STOCHASTIC
        if not self.isDeterministic:
            self.set_heuristics()

    def calculate_ValueIterationUtility(self, prob, reward, stateNext, utility):
        return prob * (reward + self._discount * utility[stateNext])

    def calculate_PolicyIterationUtility(self, prob, reward, state, stateNext, utility):
        return reward[state] + self._discount * (prob * utility[stateNext])

    def move(self, currentNode, direction):
        if direction == 'E':
            return currentNode[0], currentNode[1] + 1
        elif direction == 'W':
            return currentNode[0], currentNode[1] - 1
        elif direction == 'N':
            return currentNode[0] - 1, currentNode[1]
        elif direction == 'S':
            return currentNode[0] + 1, currentNode[1]
