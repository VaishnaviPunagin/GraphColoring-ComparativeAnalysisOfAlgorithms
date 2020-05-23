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
    ele = int(input())
    nodes.append(ele)
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
