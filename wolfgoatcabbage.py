# CPSC 481
# Jared Castaneda
# Tiffanny Hernaez
# Sagar Joshi

from search import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial_state, goal=(1, 1, 1, 1)):
        super().__init__(initial_state, goal)
        # False --> boat is moving back to the right
        # True --> boat is moving to the left

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
       # returns the new state reached from the given state and the given action
        new_state = list(state)
        # Keep track of states

        if action == "F":
            new_state[0] = not new_state[0]
        if action == "FW":
            new_state[0] = not new_state[0]
            new_state[1] = not new_state[1]
        elif action == "FG":
            new_state[0] = not new_state[0]
            new_state[2] = not new_state[2]
        elif action == "FC":
            new_state[0] = not new_state[0]
            new_state[3] = not new_state[3]

        return tuple(new_state)

    def actions(self, state):
        possible_actions = ['F', 'FW', 'FG', 'FC']
        # FARMER 0
        # WOLF 1
        # GOAT 2
        # CABBAGE 3

        # (0 0 0 1) or (1 1 1 0) ///////// (0 1 0 0) or (1 0 1 1)
        # Farmer wolf goat on one side and cabbage is not, you can't leave because wolf and goat by themselves. If farmer goat and cabbage are on one side, can't leave because goat and cabbage are alone.
        if state[0] == state[1] == state[2] != state[3] or state[0] == state[2] == state[3] != state[1]:
            possible_actions.remove("F")

        # Cross the river
        if state[0] != state[1]:
            # Can't move wolf because farmer and wolf on opposite sides
            possible_actions.remove("FW")
        if state[0] != state[2]:
            # Can't move goat because farmer and goat on opposite sides
            possible_actions.remove("FG")
        if state[0] != state[3]:
            # Can't move cabbage because farmer and cabbage on opposite sides
            possible_actions.remove("FC")

        # All on one side. Goat will eat cabbage (Cant move wolf) and wolf will eat goat (Cant move goat) if left alone.
        if state[0] == state[1] == state[2] == state[3]:
            # Goat eats cabbage so you can't move wolf to leave GC alone
            possible_actions.remove("FW")
            # Wolf eats goat so you can't move cabbage to leave WG alone
            possible_actions.remove("FC")

        return possible_actions


if __name__ == '__main__':
    initial = (1, 0, 0, 0)
    wgc = WolfGoatCabbage(initial)
    print("Depth first graph search:")
    solution = depth_first_graph_search(wgc).solution()
    print(solution)

    print("\n\nBreadth first graph search:")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
