import generate
import dfs

adjacency_matrix = generate.generate_adjacency_matrix(10000)
edge_list = generate.generate_edge_list(10000,adjacency_matrix)
list_of_next_elements = generate.generate_list_of_next_elements(5,adjacency_matrix)
#print("edge list {}".format(str(edge_list)))

print("dfs {}".format(dfs.dfs_edge_list(10000,edge_list)))
