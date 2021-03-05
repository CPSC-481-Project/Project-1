from search import *
# YOUR CODE GOES HERE

# Constructor setting initial and goal states


class WoldGoatCabbage():
    initial = {"Wolf", "Goat", "Cabbage"}


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)


# NEW CODE FROM THE HOMIES


# Constructor setting initial and goal states

'''
Consider the following puzzle: A farmer (F) with his wolf (W), goat (G), and cabbage (C)
 come to the left bank of a river they wish to cross.
There is a boat at the river's edge that can carry at most two things across 
the river at a time, one of which must be the farmer. 
If the wolf is ever left alone with the goat, the wolf will eat the goat. 
If the goat is left alone with the cabbage, the goat will eat the cabbage. 
The puzzle is to come up with a sequence of river crossings so that all four characters 
arrive safely on the other side of the river.
One way to represent the states of this problem is with two sets, the characters on the
 left and right banks of the river respectively. 
For example: {F,G},{W,C} represents the farmer and goat on one bank, and the wolf and cabbage on the other.'''


class test:
    invalid_scenarios = [
        ["C", "G", "W"],
        ["G", "W"],
        ["C", "G"]
    ]

    def __init__(self, left=["W", "C", "G"], right=[], boat_side=False):
        self.left = left
        self.right = right
        self.boat_side = boat_side

    def __str__(self):
        return str(self.left) + str(self.right) + ("Left" if not self.boat_side else "Right")

    def state_of():
        try:

            # End of sagar's brain


class WolfGoatCabbage(Problem):

    def __init__(self, initial, goal, goal_state):
        self.initial = State{"F", "W", "G", "C"}  # left side of river
        goal_state = State(
            F=Location.A,
            W=Location.A.
            G=Location.A,
            C=Location.A,
        )
        self.goal = {}  # left side of river at the end

    def goal_test(self, state):
        # returns True if the given state is a goal state
        return state == self.goal

    def result(self, state, action):
        # returns the new state reached from the given state and the given action
        return None

    def actions(self, state):
        # turns a list of valid actions in the given state
        # checks for constraints
        def goat_eats_cabbage = (
            state.G == state.C
            and state.man != state.G
        )
        # Let this be what we can attempt to do
        possible_group = ["F", "G", "C", "W"]


#[{'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {'F'}, {'G', 'F'}]
#[{'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'}, {'C', 'F'}, {'F'}, {'G', 'F'}]

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
