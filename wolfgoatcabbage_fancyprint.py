from search import *

# Constructor setting initial and goal states
possible_actions_fancy = []


class WolfGoatCabbage(Problem):
    # (F, W, G, C)

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
        if action[0] == "[C,F]":
            # Keep track of states
            if new_state[4] == True:
                # Boat currently on left island and will move Cabbage to the right island
                new_state[3] = 1
                new_state[4] = not new_state[4]
            else:
                # Boat currently on the right island and will move Cabbage to the left island
                new_state[3] = 0
        elif action[0] == "[W,F]":
            # Keep track of states
            if new_state[4] == True:
                # Boat currently on the left island and will move Wolf to the right island
                new_state[1] = 1
                new_state[4] = not new_state[4]
            else:
                # Boat currently on the right island and will move Wolf to the left island
                new_state[1] = 0

        elif action[0] == "[G,F]":
            # Keep track of states
            if new_state[4] == True:
                # Goat moving on the right island
                new_state[2] = 1
                new_state[4] = not new_state[4]  # Changing to false
            else:
                # Goat moving on the left island
                new_state[2] = 0
                new_state[4] = not new_state[4]

        elif action[0] == "[F]":
            if new_state[4] == False:
                # Farmer is on left island now and will move back to right island
                new_state[4] = True

        return tuple(new_state)

    def actions(self, state):
        # NEW FANCYPRINT !!!! This will return an array, with the action and the fancyprint.
        #[ 'Action', 'Fancyprint']

        # Make sure no bad movements occur
        possible_actions = []  # 'FC', 'FW', 'FG'
        possible_actions2 = []
        # (F, W, G, C, Position)

        # Possible actions per scenario on the right island:
        # False --> boat coming from right
        # True --> boat coming from left

        # Nothing is on the right island..moving any possible item to the right
        if state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action
            possible_actions.append("[G,F]")
            possible_actions.append("Farmer and Goat move to the right")
            possible_actions2.append(possible_actions)

        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action after moving goat..going back to left island
            # Coming from right island
            possible_actions.append("[F]")
            possible_actions.append("Farmer moves to the left")
            possible_actions2.append(possible_actions)

        # Goat is currently on the right island..boat has returned to the right island
        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move wolf to left island
            possible_actions.append("[W,F]")
            possible_actions.append("Farmer and Wolf move to the right")
            # Can't bring cabbage --> Goat will devour\
            possible_actions2.append(possible_actions)

        # Wolf and Goat is currently on the right island but cannot stay together
        if state[1] == 1 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action to return Goat on left island
            possible_actions.append("[G,F]")
            possible_actions.append("Farmer and Goat move to the left")
            possible_actions2.append(possible_actions)

        # Wolf is currently on right island and is moving cabbage to right island
        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move cabbage to right island
            possible_actions.append("[C,F]")
            possible_actions.append("Farmer and Cabbage move to the right")
            possible_actions2.append(possible_actions)

        # if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == False:
        #     # Currently Farmer's action after moving cabbage...going back to left island
        #     possible_actions.append("[F]")
        #     possible_actions.append("Farmer moves to the left")
        #     possible_actions2.append(possible_actions)

        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action after moving cabbage...going back to left island
            possible_actions.append("[F]")
            possible_actions.append("Farmer moves to the left")
            possible_actions2.append(possible_actions)

        # Wolf and Cabbage currently on the right island
        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == True:
            # Currently Farmer's action to move Goat to right island
            possible_actions.append("[G,F]")
            possible_actions.append("Farmer and Goat move to the right")
            possible_actions2.append(possible_actions)

        if state[1] == 1 and state[2] == 1 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action to move Goat to right island
            possible_actions.append("[F,W,G,C]")
            possible_actions.append("End of actions. Goal state reached.")
            possible_actions2.append(possible_actions)

        return possible_actions

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage()
    sol = depth_first_graph_search(wgc)
    sol = breadth_first_graph_search(wgc)

    # Variable is the right side only and initial only
    print(wgc.actions(initial)[1])  # Print second element, which is the action
    pos_states = ["FG", "F", "FW", "FG", "FC", "F", "FG"]
    current_state = initial
    for x in pos_states:
        temp_state = wgc.result(current_state, wgc.actions(current_state))
        current_state = temp_state
        # Print second element, which is the action
        print(wgc.actions(current_state)[1])
        # print(current_state)
