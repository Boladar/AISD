import generate
import dfs

adjacency_matrix = generate.generate_adjacency_matrix(500)
edge_list = generate.generate_edge_list(500,adjacency_matrix)
list_of_next_elements = generate.generate_list_of_next_elements(5,adjacency_matrix)
print("edge list {}".format(edge_list))

print("dfs {}".format(dfs.dfs_edge_list(500,edge_list)))
