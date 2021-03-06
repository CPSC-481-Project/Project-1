from search import *
# YOUR CODE GOES HERE

# Constructor setting initial and goal states


class WolfGoatCabbage(Problem):
    # bad_states = [
    #     ["C", "G", "W"],
    #     ["G", "W"],
    #     ["C", "G"]
    # ]
    # goal = [True, True, True]

    # def __init__(self, left=["W", "C", "G"], positionState=[False, False, False], right=[], boat=False):
    #     self.left = left
    #     self.right = right
    #     self.boat = boat
    #     self.position = position

    # def goal_test(self):
    #     return self.position == self.goal

    # def result(self, state, action):
    #     # returns the new state reached from the given state and the given action
    #     if "W" in self.right and "C" in self.right and "G" in self.right and self.boat == True:
    #         return self.positionState = goal
    #     elif "W" in self.right and "C" in self.right and self.boat == True:
    #         return self.positionState = [True, True, False]
    #     elif "W" in self.right and self.boat == True:
    #         return self.positionState = [True, False, False]
    #     elif "C" in self.right and self.boat == True:
    #         retrun self.positionState = [False, True, False]
    #     elif "G" in self.right and self.boat == True:
    #         return self.positionState = [False, False, True]

    # def actions(self, state):
    #     # that returns a list of valid actions in the given state
    # (F, W, G, C)
    def __init__(self, initial=(1, 0, 0, 0, True), goal=(1, 1, 1, 1, False)):
        self.initial = initial
        self.goal = goal
        # False --> boat is moving back to the right
        # True --> boat is moving to the left

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        # def result(self, state, action):
        #     """ Given state and action, return a new state that is the result of the action.
        #     Action is assumed to be a valid action in the state """

        #     # blank is the index of the blank square
        #     blank = self.find_blank_square(state)
        #     new_state = list(state)

        #     delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        #     neighbor = blank + delta[action]
        #     new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        #     return tuple(new_state)

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
        # Make sure no bad movements occur

        # def actions(self, state):
        #     """ Return the actions that can be executed in the given state.
        #     The result would be a list, since there are only four possible actions
        #     in any given state of the environment """

        #     possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        #     index_blank_square = self.find_blank_square(state)

        #     if index_blank_square % 3 == 0:
        #         possible_actions.remove('LEFT')
        #     if index_blank_square < 3:
        #         possible_actions.remove('UP')
        #     if index_blank_square % 3 == 2:
        #         possible_actions.remove('RIGHT')
        #     if index_blank_square > 5:
        #         possible_actions.remove('DOWN')

        #     return possible_actions

        possible_actions = []  # 'FC', 'FW', 'FG'

        # (F, W, G, C, Position)

        # Possible actions per scenario on the right island:
        # False --> boat coming from right
        # True --> boat coming from left

        # Nothing is on the right island..moving any possible item to the right
        if state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action
            possible_actions.append("[G,F]")
            # possible_actions.append('FC')

        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action after moving goat..going back to left island
            # Coming from right island
            possible_actions.append("[F]")

        # Goat is currently on the right island..boat has returned to the right island
        if state[1] == 0 and state[2] == 1 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move wolf to left island
            possible_actions.append("[W,F]")
            # Can't bring cabbage --> Goat will devour

        # Wolf and Goat is currently on the right island but cannot stay together
        if state[1] == 1 and state[2] == 1 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action to return Goat on left island
            possible_actions.append("[G,F]")

        # Wolf is currently on right island and is moving cabbage to right island
        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
            # Currently Farmer's action to move cabbage to right island
            possible_actions.append("[C,F]")
            # state[3] = 1

        if state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == False:
            # Currently Farmer's action after moving cabbage...going back to left island
            possible_actions.append("[F]")

        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action after moving cabbage...going back to left island
            possible_actions.append("[F]")

        # Wolf and Cabbage currently on the right island
        if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == True:
            # Currently Farmer's action to move Goat to right island
            possible_actions.append("[G,F]")
            # state[2] = 1

        if state[1] == 1 and state[2] == 1 and state[3] == 1 and state[4] == False:
            # Currently Farmer's action to move Goat to right island
            possible_actions.append("[F,W,G,C]")

        return possible_actions

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage()
    sol = depth_first_graph_search(wgc)
    # print(sol)
    sol = breadth_first_graph_search(wgc)
    # print(sol)

    # Variable is the right side only and initial only
    print(wgc.actions(initial))
    pos_states = ["FG", "F", "FW", "FG", "FC", "F", "FG"]
    current_state = initial
    for x in pos_states:
        # while wgc.goal_test:
        temp_state = wgc.result(current_state, wgc.actions(current_state))
        current_state = temp_state
        # initial = (1, 0, 1, 0, False)
        print(wgc.actions(current_state))
        # print(current_state)
