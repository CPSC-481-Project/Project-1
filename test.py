import sys
from collections import deque

from utils import *
from search import *


class MissCannibals(Problem):

    # state is 3 tuple (m,c,onLeft)
    def __init__(self, initial, goal=(0, 0, False)):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        new_state = list(state)

        # possible actions: MM, MC, CC, M, C
        if action == 'MM':
            # if boat is moving to the right
            if new_state[2] == True:
                new_state[0] -= 2
            # otherwise, boat is moving to the left
            else:
                new_state[0] += 2
        if action == 'MC':
            if new_state[2] == True:
                new_state[0] -= 1
                new_state[1] -= 1
            else:
                new_state[0] += 1
                new_state[1] += 1
        if action == 'CC':
            if new_state[2] == True:
                new_state[1] -= 2
            else:
                new_state[1] += 2
        if action == 'M':
            if new_state[2] == True:
                new_state[0] -= 1
            else:
                new_state[0] += 1
        if action == 'C':
            if new_state[2] == True:
                new_state[1] -= 1
            else:
                new_state[1] += 1

        new_state[2] = not new_state[2]
        return tuple(new_state)

    def actions(self, state):
        possible_actions = []

        if state[0] == 3 and state[1] == 3 and state[2] == True:
            possible_actions.append('MC')
            possible_actions.append('CC')
            possible_actions.append('C')
        if state[0] == 2 and state[1] == 2 and state[2] == False:
            possible_actions.append('MC')
            possible_actions.append('M')
        if state[0] == 3 and state[1] == 1 and state[2] == False:
            possible_actions.append('CC')
            possible_actions.append('C')
        if state[0] == 3 and state[1] == 2 and state[2] == False:
            possible_actions.append('C')
        if state[0] == 3 and state[1] == 2 and state[2] == True:
            possible_actions.append('M')
            possible_actions.append('C')
            possible_actions.append('CC')
        if state[0] == 3 and state[1] == 0 and state[2] == False:
            possible_actions.append('CC')
            possible_actions.append('C')
        if state[0] == 3 and state[1] == 1 and state[2] == True:
            possible_actions.append('C')
            possible_actions.append('MM')
        if state[0] == 1 and state[1] == 1 and state[2] == False:
            possible_actions.append('MM')
            possible_actions.append('MC')
        if state[0] == 2 and state[1] == 2 and state[2] == True:
            possible_actions.append('MC')
            possible_actions.append('MM')
        if state[0] == 0 and state[1] == 2 and state[2] == False:
            possible_actions.append('MM')
            possible_actions.append('C')
        if state[0] == 0 and state[1] == 3 and state[2] == True:
            possible_actions.append('C')
            possible_actions.append('CC')
        if state[0] == 0 and state[1] == 1 and state[2] == False:
            possible_actions.append('C')
            possible_actions.append('M')
        if state[0] == 0 and state[1] == 1 and state[2] == True:
            possible_actions.append('C')
        if state[0] == 0 and state[1] == 2 and state[2] == True:
            possible_actions.append('CC')
        if state[0] == 1 and state[1] == 1 and state[2] == True:
            possible_actions.append('MC')
        if state[0] == 0 and state[1] == 0 and state[2] == False:
            possible_actions.append('C')
            possible_actions.append('CC')
            possible_actions.append('MC')

        return possible_actions


if __name__ == '__main__':
    initial_state = (3, 3, True)
    misscann = MissCannibals(initial_state)
    path = depth_first_graph_search(misscann).solution()
    print(path)

    states = ['CC', 'C', 'CC', 'C', 'MM', 'MC', 'MM', 'C', 'CC', 'M', 'MC']
    print(initial_state)
    current_state = initial_state
    for x in states:
        current_state = misscann.result(current_state, x)
        print(current_state)
