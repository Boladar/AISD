import generate
import dfs
import sys

sys.setrecursionlimit(5000)

def print_adjacency_matrix(n,graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print("")

adjacency_matrix = generate.generate_adjacency_matrix(5)
print_adjacency_matrix(5,adjacency_matrix)
print(generate.generate_edge_list(5,adjacency_matrix))
print(generate.generate_list_of_next_elements(5,adjacency_matrix))

print(dfs.dfs_adjacency_matrix(5,adjacency_matrix))