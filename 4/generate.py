import random

def print_list_of_next_elements(n,next_dictionary):
    for i in range(n):
        print("{} : {}".format(i,next_dictionary[i]))

def print_graph(n,graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print("")


def calculate_saturation_rate(n,percent):
    return int((n*(n-1)/2)*percent)

def pick_node(visited,current_node,size):
    choice = current_node
    while choice in visited or choice == current_node:
        choice = random.randint(0,size-1)
    return choice

def add_edge(next_dictionary,current_node,next_node):
    next_dictionary[current_node].append(next_node)
    next_dictionary[next_node].append(current_node)

def generate_graph(size,saturation):
    next_dictionary = {}
    visited = []

    for i in range(size):
        next_dictionary[i] = [] 

    current_node = 0
    for i in range(size-1):
        visited.append(current_node)
        next_node = pick_node(visited,current_node,size)
        add_edge(next_dictionary,current_node,next_node)
        current_node = next_node

    #make sure it's a cycle
    add_edge(next_dictionary,current_node,0)


    current_saturation = size
    saturation = calculate_saturation_rate(size,saturation)
    print(saturation)
    while saturation - current_saturation > 2:
        picked_node = random.randint(0,size-1)
        picked_node_next = next_dictionary[picked_node]

        add_edge(next_dictionary,picked_node_next[0],picked_node_next[1])

        picked_supplemental_node = picked_node
        while picked_supplemental_node == picked_node or picked_supplemental_node in picked_node_next:
            picked_supplemental_node = random.randint(0,size-1)

        add_edge(next_dictionary,picked_supplemental_node,picked_node_next[0])
        add_edge(next_dictionary,picked_supplemental_node,picked_node_next[1])

        current_saturation += 3


    print_list_of_next_elements(size,next_dictionary)