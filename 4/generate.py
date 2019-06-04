import random

def print_list_of_next_elements(next_dictionary):
    for i in range(len(next_dictionary)):
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

    if current_node == next_node:
        raise Exception("trying to add edge to itself {}".format(current_node))

    if next_node in next_dictionary[current_node]:
        raise Exception("trying to add existing edge once more {} ->{} ".format(current_node,next_node))

    next_dictionary[current_node].append(next_node)
    next_dictionary[next_node].append(current_node)

def pick_not_connected_next_nodes(next_dictionary,node):
    next_elements = next_dictionary[node]
    for i in range(len(next_elements)):
        previous = next_elements[i]
        for j in range(i,len(next_elements)):
            next = next_elements[j]

            if next not in next_dictionary[previous] and previous != next:
                return [previous,next]

    return None
            
    
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
    wanted_edge_saturation = calculate_saturation_rate(size,saturation)
    not_viable_nodes = []
    while wanted_edge_saturation - current_saturation > 2:

        picked_node = random.randint(0,size-1)
        picked_node_next = next_dictionary[picked_node]
        picked_nodes = False
        not_viable_nodes.clear()
        while not picked_nodes:
            #print(next_dictionary[picked_node_next[0]])
            picked_node = random.randint(0,size-1)

            if picked_node in not_viable_nodes:
                continue

            picked_node_next = pick_not_connected_next_nodes(next_dictionary,picked_node)

            if picked_node_next is None:
                not_viable_nodes.append(picked_node)
                continue
            else:
                if picked_node_next[0] not in next_dictionary[picked_node_next[1]]:
                    picked_nodes = True

        add_edge(next_dictionary,picked_node_next[0],picked_node_next[1])

        picked_supplemental_node = None
        for i in range(size):
            potential_supplemental_node = i
            if (potential_supplemental_node != picked_node and
                potential_supplemental_node not in next_dictionary[picked_node_next[0]] and
                potential_supplemental_node not in next_dictionary[picked_node_next[1]]):
                picked_supplemental_node = potential_supplemental_node

        if picked_supplemental_node is None:
            return None

        add_edge(next_dictionary,picked_supplemental_node,picked_node_next[0])
        add_edge(next_dictionary,picked_supplemental_node,picked_node_next[1])

        current_saturation += 3

    return next_dictionary