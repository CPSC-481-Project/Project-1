from search import *

# Constructor setting initial and goal states


class WolfGoatCabbage(Problem):
    # (F, W, G, C)
    def __init__(self, initial_state, goal=(True, True, True, True, False)):
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

        # Change from t to f or f to t
        new_state[4] = not new_state[4]

        return tuple(new_state)

    def actions(self, state):
        possible_actions = ['F', 'W', 'G', 'C']  # 'FC', 'FW', 'FG'

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
            print("[G,F]")
            possible_actions.remove("W")
            possible_actions.remove("C")

        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action after moving goat..going back to left island
            # Coming from right island
            print("[F]")
            possible_actions.remove("W")
            possible_actions.remove("G")
            possible_actions.remove("C")

        # Goat is currently on the right island..boat has returned to the right island
        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move wolf to left island
            print("[W,F]")
            possible_actions.remove("G")
            possible_actions.remove("C")
            # Can't bring cabbage --> Goat will devour

        # Wolf and Goat is currently on the right island but cannot stay together
        if state[1] == 1 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action to return Goat on left island
            # possible_actions.append("[G,F]")
            print("[G,F]")
            possible_actions.remove("W")
            possible_actions.remove("C")

        # Wolf is currently on right island and is moving cabbage to right island
        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move cabbage to right island
            print("[C,F]")
            possible_actions.remove("W")
            possible_actions.remove("G")

        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action after moving cabbage...going back to left island
            print("[F]")
            possible_actions.remove("W")
            possible_actions.remove("G")
            possible_actions.remove("C")

        # Wolf and Cabbage currently on the right island
        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == True:
            # Currently Farmer's action to move Goat to right island
            print("[G,F]")
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

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage(initial)
    print("This is DFS:")
    solution = depth_first_graph_search(wgc).solution()
    print(solution)

    print("\n\nThis is BFS:")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
