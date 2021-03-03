from search import *
# YOUR CODE GOES HERE

# Constructor setting initial and goal states
class WolfGoatCabbage():
 
 
 
 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
