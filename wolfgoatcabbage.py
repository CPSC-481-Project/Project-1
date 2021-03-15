#CPSC 481
# Jared Castaneda
# Tiffanny Hernaez
# Ricardo martinez

rom search import *

# Constructor setting initial and goal states


class WolfGoatCabbage(Problem):
    # (F, W, G, C)
    def __init__(self, initial_state, goal=(1, 1, 1, 1)):
        super().__init__(initial_state, goal)
        # False --> boat is moving back to the right
        # True --> boat is moving to the left

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
       # returns the new state reached from the given state and the given action
        new_state = list(state)
        # Possible actions on the boat
        # (F, W, G, C, Position)
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

        # (F, W, G, C,)
        # FARMER 0
        # WOLF 1
        # GOAT 2
        # CABBAGE 3

        # (0 0 0 1) or (1 1 1 0) ///////// (0 1 0 0) or (1 0 1 1)
        #Farmer wolf goat on one side and cabbage is not, you can't leave because wolf and goat by themselves. If farmer goat and cabbage are on one side, can't leave because goat and cabbage are alone.
        if state[0] == state[1] == state[2] != state[3] or state[0] == state[2] == state[3] != state[1]:
            possible_actions.remove("F")

        #Cross the river
        if state[0] != state[1]:
            possible_actions.remove("FW") #Can't move wolf because farmer and wolf on opposite sides
        if state[0] != state[2]:
            possible_actions.remove("FG") #Can't move goat because farmer and goat on opposite sides
        if state[0] != state[3]:
            possible_actions.remove("FC") #Can't move cabbage because farmer and cabbage on opposite sides    
        
        # All on one side. Goat will eat cabbage (Cant move wolf) and wolf will eat goat (Cant move goat) if left alone.
        if state[0] == state[1] == state[2] == state[3]:
            possible_actions.remove("FW") #Goat eats cabbage so you can't move wolf to leave GC alone
            possible_actions.remove("FC") #Wolf eats goat so you can't move cabbage to leave WG alone

        return possible_actions
        
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':
    initial = (1, 0, 0, 0)
    wgc = WolfGoatCabbage(initial)
    print("Depth first graph search:")
    solution = depth_first_graph_search(wgc).solution()
    print(solution)

    print("\n\nBreadth first graph search:")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
