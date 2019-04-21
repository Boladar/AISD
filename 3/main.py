import generate

def print_adjacency_graph(n,graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print("")

adjacency_matrix = generate.generate_adjacency_graph(5)
print_adjacency_graph(5,adjacency_matrix)
print(generate.generate_edge_list(5,adjacency_matrix))