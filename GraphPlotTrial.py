import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
G = nx.MultiDiGraph()
n = int(input("Enter number of colours : "))
colors = []
for i in range(0, n):
    print("Enter the %d color:" % (i+1))
    ele = input()
    colors.append(ele)
print(colors)
x = int(input("Enter number of nodes : "))
nodes = []
for i in range(0, x):
    print("Enter the %d node " % (i+1))
    ele = input()
    G.add_node(ele)
    nodes.append(ele)
print(G.nodes)
print(nodes)
neighbors = {}
for i in range(0, x):
    key = nodes[i]
    print("Enter the number of connections for the node %s:" % key)
    z = int(input())
    my_list = []
    for state in range(0, z):
        ele = input()
        G.add_edge(key, ele)
        my_list.append(ele)

    neighbors.update({key: my_list})
print(G.edges)

# for num1, num2 in G[num1][num2][0]:
#     if(num1 == num2):
#         G[num1][num2][0]['color'] = 'red'
# G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
# G.graph['graph'] = {'scale': '3', 'color': 'red'}
nx.draw(G)
plt.savefig("simple_path.png")  # save as png
plt.show()  # display
# A = to_agraph(G)
# A.layout('dot')
# A.draw('multi.png')
