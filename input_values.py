
colors = ["r","b","g","y"]

x = int(input("Enter number of nodes : "))
nodes = []
for i in range(0, x):
    nodes.append(i+1)
print(nodes)
neighbors = {}
for i in range(0, x):
    key = nodes[i]
    print("Enter the number of connections for {%d}:" % key)
    z = int(input())
    my_list = []
    for state in range(0, z):
        ele = int(input())
        my_list.append(ele)
    neighbors.update({key: my_list})
