import time

n = int(input("Enter number of colours : "))

colors = []
for i in range(0, n):
    ele = input()

    colors.append(ele)

print(colors)
x = int(input("Enter number of states : "))

states = []
for i in range(0, x):
    ele = input()

    states.append(ele)

print(states)
neighbors = {}


for i in range(0, x):
    key = states[i]
    print("Enter the number of connections for {%s}:" % key)
    z = int(input())
    my_list = []
    for state in range(0, z):
        ele = input()
        my_list.append(ele)
    neighbors.update({key: my_list})


# print(neighbors)


colors_of_states = {}


def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True


def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color


def main():

    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print(colors_of_states)
   
#starting time
start =  time.time()
main()
#sleeping for 1 second to get 10 seconds runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

tt=end-start 
# total time taken
print("Runtime of the program is")
print(tt)
