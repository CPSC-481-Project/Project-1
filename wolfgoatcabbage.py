from search import *

# Constructor setting initial and goal states


class WolfGoatCabbage(Problem):
    # (F, W, G, C)
    def __init__(self, initial_state, goal=(1, 1, 1, 1, False)):
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

        for x in action:
            if x == "W":
                new_state[1] = not new_state[1]
            elif x == "G":
                new_state[2] = not new_state[2]
            elif x == "C":
                new_state[3] = not new_state[3]
            
        #Change from t to f or f to t
        new_state[4] = not new_state[4]

        return tuple(new_state)

    def actions(self, state):
        possible_actions = ['F','W', 'G', 'C']  # 'FC', 'FW', 'FG'
        


        # (F, W, G, C, Position)
        # FARMER 0
        # WOLF 1
        # GOAT 2
        # CABBAGE 3
        # POS 4

        # Possible actions per scenario on the right island:
        # False --> boat coming from right
        # True --> boat coming from left

        # Nothing is on the right island..moving any possible item to the right
        if state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action
            # possible_actions.append("[G,F]")
            # possible_actions.append('FC')
            possible_actions.remove("W")
            possible_actions.remove("C")

        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action after moving goat..going back to left island
            # Coming from right island
            possible_actions.remove("W")
            possible_actions.remove("G")
            possible_actions.remove("C")

        # Goat is currently on the right island..boat has returned to the right island
        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move wolf to left island
            possible_actions.remove("G")
            possible_actions.remove("C")
            # Can't bring cabbage --> Goat will devour

        # Wolf and Goat is currently on the right island but cannot stay together
        if state[1] == 1 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action to return Goat on left island
            #possible_actions.append("[G,F]")
            possible_actions.remove("W")
            possible_actions.remove("C")

        # Wolf is currently on right island and is moving cabbage to right island
        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move cabbage to right island
            possible_actions.remove("W")
            possible_actions.remove("G")

        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action after moving cabbage...going back to left island
            possible_actions.remove("W")
            possible_actions.remove("G")
            possible_actions.remove("C")

        # Wolf and Cabbage currently on the right island
        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == True:
            # Currently Farmer's action to move Goat to right island
            possible_actions.remove("W")
            possible_actions.remove("C")

        if state[1] == 1 and state[2] == 1 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action to move Goat to right island
            possible_actions.remove("F")
            possible_actions.remove("G")
            possible_actions.remove("W")
            possible_actions.remove("C")

        return possible_actions

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return (len(node.state)/2)


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage(initial)
    solution = depth_first_graph_search(wgc).solution()
    print(solution) 
    print("This is DFS")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    print("This is BFS")
    
    # Variable is the right side only and initial only
    print(h())
    print(wgc.actions(initial))

    current_state = initial
    while not wgc.goal_test(current_state):
        temp_state = wgc.result(current_state, wgc.actions(current_state))
        current_state = temp_state
        print(wgc.actions(current_state))
        # print(current_state)


"""
    Take the goat over
    Return
    Take the wolf or cabbage over
    Return with the goat
    Take the cabbage or wolf over
    Return
    Take goat over
"""


"""
['G', 'F', 'W', 'G', 'C', 'F', 'G'] - DFS
['F', 'W', 'F', 'G', 'C'] - BFS
['F', 'G']
['F']
['F', 'W']
['F', 'G']
['F', 'C']
['F']
['F', 'G']
[]
"""
