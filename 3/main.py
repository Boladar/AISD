import generate

def print_adjacency_graph(n,graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print("")

print_adjacency_graph(5,generate.generate_adjacency_graph(5))
print("expected saturation rate: {}".format(generate.calculate_saturation_rate(5)))