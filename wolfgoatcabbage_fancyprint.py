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
        elif action == "FW":
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
        possible_actions = ['F', 'FG', 'FW', 'FC']
        # FARMER 0
        # WOLF 1
        # GOAT 2
        # CABBAGE 3
        # POS 4

        # Possible actions per scenario on the right island:
        if state[0] != state[1]:
            # Farmer and Wolf not on the same side
            possible_actions.remove("FW")
        if state[0] != state[2]:
            # Famer and goat not on the same side
            possible_actions.remove("FG")
        if state[0] != state[3]:
            # Farmer and cabbage not on the same side
            possible_actions.remove("FC")

        if state[0] == state[1] == state[2] == state[3]:
            # Goat eats cabbage so you can't move wolf to leave GC alone
            possible_actions.remove("FW")
            # Wolf eats goat so you can't move cabbage to leave WG alone
            possible_actions.remove("FC")

        # Wolf and Goat cannot be on same side alone
        # Goat and Cabbaga cannot be on the same side alone
        if state[0] == state[1] == state[2] != state[3] or state[0] == state[2] == state[3] != state[1]:
            possible_actions.remove("F")

        # print(state)
        return possible_actions


if __name__ == '__main__':
    initial = (0, 0, 0, 0)
    wgc = WolfGoatCabbage(initial)

    # PRINTING OUT FANCY PRINT FOR DFS
    print("DFS:")
    sol = depth_first_graph_search(wgc).solution()
    print(sol)
    current_state = initial
    for x in sol:
        current_state = wgc.result(current_state, x)
        # print(current_state)
        if current_state[0] == True and current_state[1] == False and current_state[2] == True and current_state[3] == False:
            print("Farmer & Goat crosses")
        if current_state[0] == False and current_state[1] == False and current_state[2] == True and current_state[3] == False:
            print("Farmer is crossing back")
        if current_state[0] == True and current_state[1] == False and current_state[2] == True and current_state[3] == True:
            print("Farmer & Cabbage crosses")
        if current_state[0] == False and current_state[1] == False and current_state[2] == False and current_state[3] == True:
            print("Farmer & Goat crosses back")
        if current_state[0] == True and current_state[1] == True and current_state[2] == False and current_state[3] == True:
            print("Farmer & Wolf crosses")
        if current_state[0] == False and current_state[1] == True and current_state[2] == False and current_state[3] == True:
            print("Farmer crosses back")
        # GOAL STATE
        if current_state[0] == True and current_state[1] == True and current_state[2] == True and current_state[3] == True:
            print("Farmer & Goat crosses")

    # PRINTING OUT FANCY PRINT FOR BFS
    print("\n\nBFS:")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    current_state = initial
    for x in sol:
        current_state = wgc.result(current_state, x)
        if current_state[0] == True and current_state[1] == False and current_state[2] == True and current_state[3] == False:
            print("Farmer & Goat crosses")
        if current_state[0] == False and current_state[1] == False and current_state[2] == True and current_state[3] == False:
            print("Farmer crosses back")
        if current_state[0] == True and current_state[1] == False and current_state[2] == True and current_state[3] == True:
            print("Farmer & Wolf crosses")
        if current_state[0] == False and current_state[1] == False and current_state[2] == False and current_state[3] == True:
            print("Farmer & Goat crosses back")
        if current_state[0] == True and current_state[1] == True and current_state[2] == False and current_state[3] == True:
            print("Farmer & Cabbage crosses")
        if current_state[0] == False and current_state[1] == True and current_state[2] == False and current_state[3] == True:
            print("Farmer crosses back")
        # GOAL STATE
        if current_state[0] == True and current_state[1] == True and current_state[2] == True and current_state[3] == True:
            print("Farmer & Goat crosses")
