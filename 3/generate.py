import random

def calculate_saturation_rate(n):
    return int((n*(n-1)/2)/2)

def generate_adjacency_graph(n):
    graph = []

    random_list = [i for i in range(1,int(n*(n-1)/2))]
    random.shuffle(random_list)
    size = calculate_saturation_rate(n)
    random_list = random_list[:size]
    random_list.sort()

    print (random_list)

    random_index = 0
    field_number = 0
    for i in range(n):
        row = []
        for j in range(n):
            if  i == j:
                row.append(0)   #diagonal
            elif j > i: # upper triangle
                if len(random_list) > random_index:
                    if random_list[random_index] == field_number:
                        row.append(1)
                        random_index += 1
                        
                    else:
                        row.append(0)
                else:
                    row.append(0)

                field_number += 1

            else:
                row.append(0)

        graph.append(row)
    
    return graph

def generate_edge_list(n,adjacency_matrix):
    edge_list = []
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j]:
                edge_list.append([i,j])
    return edge_list

def generate_list_of_next_elements(n,adjacency_matrix):
    pass