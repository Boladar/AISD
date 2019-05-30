import generate
import dfs
import bfs
n = 5
adjacency_matrix = generate.generate_adjacency_matrix(n)
edge_list = generate.generate_edge_list(n,adjacency_matrix)
list_of_next_elements = generate.generate_list_of_next_elements(n,adjacency_matrix)
print(" list {}".format(str(list_of_next_elements)))

print("dfs {}".format(dfs.dfs_adjacency_matrix(n,adjacency_matrix)))
