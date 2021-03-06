from search import *
from utils import * 
# YOUR CODE GOES HERE

# Constructor setting initial and goal states


class WolfGoatCabbage(Problem):
    def __init__(self, initial=(1, 0, 0, 0, True), goal=(1, 1, 1, 1, False)):
        self.initial = initial
        self.goal = goal
        # False --> boat is moving back to the right
        # True --> boat is moving to the left

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):


       # returns the new state reached from the given state and the given action
        new_state = list(state)
    #    Possible actions on the boat
        # (F, W, G, C, Position)
        # if action == "WCFG":
        # Keep track of states

        if action == "FW":
            # Keep track of states
            if new_state[4] == True:
                # Boat currently on the left island and will move Wolf to the right island
                new_state[1] = 1
                new_state[4] = not new_state[4]
            else:
                # Boat currently on the right island and will move Wolf to the left island
                new_state[1] = 1

        elif action == "FG":
            # Keep track of states
            if new_state[4] == True:
                # Boat currently on the left island and will move Goat to the right island
                new_state[2] = 1
                new_state[4] = not new_state[4]
            else:
                # Boat currently on the right island and will move Goat to the left island
                new_state[2] = 0
        # elif action == "FWC":
            # Keep track of states

        return tuple(new_state)

    def actions(self, state):
        # Make sure no bad movements occur


        possible_actions = []  # 'FC', 'FW', 'FG'
        # (F, W, G, C, Position)

        # 0 - left island
        # 1 - right island

        # Possible actions per scenario on the right island:
        # False --> boat on the right
        # True --> boat on the left

        # Nothing is on the right island..moving any possible item to the right
        if state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == True:
            possible_actions.append('FW')
            possible_actions.append('FG')
            possible_actions.append('FC')

        # Goat is currently on the right island..boat has returned to the left island (1, 0, 1, 0, True)
        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == True:
            possible_actions.append('FW')
            # Can't bring cabbage --> Goat will devour

        # Wolf and Goat is currently on the right island but cannot stay together (1, 1, 1, 0, False) 
        if state[1] == 1 and state[2] == 1 and state[3] == 0 and state[4] == False:
            possible_actions.remove('FG')
            state[2] = 0

        # Wolf is currently on right island (1, 1, 0, 0, True)
        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
            possible_actions.append('FC')
            # state[3] = 1

        # Wolf and Cabbage currently on the right island (1, 1, 0, 1, True)
        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == True:
            possible_actions.append('FG')
            # state[2] = 1

        return possible_actions


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage()
    sol = depth_first_graph_search(wgc)
    # print(sol)
    sol = breadth_first_graph_search(wgc)
    # print(sol)
    
    #Variable is the right side result only
    # pos_states = ["FC", "FW", "FG"]
    pos_actions = wgc.actions(initial)
    current_state = initial
    for x in pos_actions:
        current_state = wgc.result(current_state, x)
        print(current_state)

# F W G C

"""
[{'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {'F'}, {'G', 'F'}]
[{'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'}, {'C', 'F'}, {'F'}, {'G', 'F'}]
"""