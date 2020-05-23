import time
from input_values import neighbors, colors

start = time.time()
# n = int(input("Enter number of colours : "))
# colors = []
# for i in range(0, n):
#     print("Enter the %d color:" % (i+1))
#     ele = input()
#     colors.append(ele)
# print(colors)
# x = int(input("Enter number of nodes : "))
# nodes = []
# for i in range(0, x):
#     print("Enter the %d node " % (i+1))
#     ele = int(input())
#     nodes.append(ele)
# print(nodes)
# neighbors = {}
# for i in range(0, x):
#     key = nodes[i]
#     print("Enter the number of connections for %d node and its connections :" % key)
#     z = int(input())
#     my_list = []
#     for state in range(0, z):
#         ele = int(input())
#         my_list.append(ele)
#     neighbors.update({key: my_list})
# colors_of_states = {}

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


if __name__ == '__main__':

    print(color_nodes(graph))
    # {'c': 0, 'a': 1, 'd': 2, 'e': 1, 'b': 2, 'f': 2}
time.sleep(1)
end = time.time()
tt = end-start
print("The time taken for welsh powell algorithm is %d" % tt)
