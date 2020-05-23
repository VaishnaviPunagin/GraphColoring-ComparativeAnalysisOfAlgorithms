import time
from gcpgy import neighbors, colors
graph = neighbors
color_map = colors


def color_nodes(graph):
    color_map = {}
    # Consider nodes in descending degree
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(
            color for color in range(len(graph)) if color not in neighbor_colors
        )
    return color_map

#starting time
start =  time.time()
if __name__ == '__main__':

    print(color_nodes(graph))
    # {'c': 0, 'a': 1, 'd': 2, 'e': 1, 'b': 2, 'f': 2}
#sleeping for 1 second to get 10 seconds runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

tt=end-start 
# total time taken
print("Runtime of the program is")
print(tt)
