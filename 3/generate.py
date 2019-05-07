import random

def calculate_saturation_rate(n):
    return int((n*(n-1)/2)/2)

def generate_graph_seed(n):
    seed = [i for i in range(1,int(n*(n-1)/2))]
    random.shuffle(seed)
    size = calculate_saturation_rate(n)
    seed = seed[:size]
    seed.sort()
    return seed

def generate_adjacency_matrix(n):
    graph = []
    seed = generate_graph_seed(n)

    random_index = 0
    field_number = 0
    for i in range(n):
        row = []
        for j in range(n):
            if  i == j:
                row.append(0)   #diagonal
            elif j > i: # upper triangle
                if len(seed) > random_index:
                    if seed[random_index] == field_number:
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
                edge_list.append(Edge(i,j))
    return edge_list

def generate_list_of_next_elements(n,adjacency_matrix):
    next_dictionary = {}
    for i in range(n):
        next_dictionary[i] = []
        for j in range(n):
            if adjacency_matrix[i][j]:
                next_dictionary[i].append(j)

    return next_dictionary

class Edge:
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def __hash__(self):
        return hash((self.l,self.r))

    def __eq__(self,other):
        return self.l == other.l and self.r == other.r

    def __str__(self):
        return "[{},{}]".format(self.l,self.r)

    def __repr__(self):
        return "[{},{}]".format(self.l,self.r)

    def __getitem__(self,index):
        if index == 0:
            return self.l
        else:
            return self.r
    