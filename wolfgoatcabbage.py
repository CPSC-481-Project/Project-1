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
        # print(node.state)
        # print(len(node.state)/2)
        return (len(2*node.state))


if __name__ == '__main__':
    initial = (1, 0, 0, 0, True)
    wgc = WolfGoatCabbage(initial)
    print("This is DFS")
    solution = depth_first_graph_search(wgc).solution()
    print(solution) 

    print("\n\nThis is BFS")
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

    print("\n\n")
    
        
    # print(current_state)
    print("\n\nHeuristic value:")
    print(wgc.h(astar_search(wgc, display = True)))

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

'''
from search import *

class WolfGoatCabbage(Problem):
    
    # Constructor (Farmer, Goat, Wolf, Cabbage)
    def __init__(self, initial, goal=(0, False)):
        super().__init__(initial, goal)

    # Returns True if the given state is a goal state
    def goal_test(self, state):
        return state == self.goal

    # Returns the new state reached from the given state and the given action
    def result(self, state, action):
    
        currentState = list(state)

        # Iterates through possible actions
        if action == {'F'}:
            if currentState[1] == True:
                currentState[0] -= 1
            else:
                currentState[0] += 1
        
        if action == {'F','G'}:
            if currentState[1] == True:
                currentState[0] -= 2
            else:
                currentState[0] += 2

        if action == {'F','W'}:
            if currentState[1] == True:
                currentState[0] -= 2
            else:
                currentState[0] += 2

        if action == {'F','C'}:
            if currentState[1] == True:
                currentState[0] -= 2
            else:
                currentState[0] += 2

        currentState[1] = not currentState[1]

        return tuple(currentState)

    # Returns a list of valid actions in the given state
    def actions(self, state):

        newActions = [{'F'}, {'F','G'}, {'F','W'}, {'F','C'}]

        if state == ('F','G'):
            newActions.remove({'F'})
            newActions.remove({'F','W'})
            newActions.remove({'F','C'})
        
        if state == ('F','W'):
            newActions.remove({'F'})
            newActions.remove({'F','G'})
            newActions.remove({'F','C'})
        
        if state == ('F','C'):
            newActions.remove({'F'})
            newActions.remove({'F','G'})
            newActions.remove({'F','W'})
        
        if state == ('F'):
            newActions.remove({'F','G'})
            newActions.remove({'F','W'})
            newActions.remove({'F','C'})

        #return newActions
        return newActions

if __name__ == '__main__':
    print("\n")
    initial_state = (4, True)

    wgc = WolfGoatCabbage(initial_state)
    

    print("DFS: ")
    ans = depth_first_graph_search(wgc).solution()
    print(ans)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    print("BFS: ")
    ans2 = breadth_first_graph_search(wgc).solution()
    print(ans2)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") 
    
    new_state = initial_state
    print(new_state)
    for i in ans:
        new_state = wgc.result(new_state, i)
        print(new_state)

    # print(wgc.actions(initial_state))
    # newState = initial_state 
    # while not wgc.goal_test(newState):
    #     temp = wgc.result(newState, wgc.actions(newState))
    #     newState = temp
    #     print(wgc.actions(newState))
    # print("\n")


#     # BFS    Left contain Wolf, Cabbage and the Boat is on the Left
#         elif state[1] == 1 and state[2] == 0 and state[3] == 0 and state[4] == True:
#             # Farmer is moving Cabbage to the Right
#             print("1Farmer and Cabbage cross")
#             newActions.remove("Goat")
#             newActions.remove("Wolf")
# # BFS    Right contains Goat, Cabagge and the Boat is on the Right
#         if state[1] == 1 and state[2] == 0 and state[3] == 1 and state[4] == False:
#             # Farmer is moving the Goat back to the Left
#             print("1Farmer and Goat cross back")
#             newActions.remove("Wolf")
#             newActions.remove("Cabbage")
# # BFS    Left contains Goat, Wolf and the Boat is on the Right
#         if state[1] == 0 and state[2] == 0 and state[3] == 1 and state[4] == True:
#             # Farmer is moving Wolf to the Right
#             print("1Farmer and Wolf cross")
#             newActions.remove("Goat")
#             newActions.remove("Cabbage")
```
