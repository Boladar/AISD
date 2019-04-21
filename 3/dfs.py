def dfs_adjacency_matrix(n,matrix):

    visited = [False for i in range(n)]
    sorted_list = []

    def  visit_node(node):
        visited[node] = True
        for j in range(n):
            if not visited[j] and matrix[node][j] == 1:
                visit_node(j)
        sorted_list.insert(0,node)

    def dfs(n,matrix):

        for i in range(n):
            if not visited[i]:
                visit_node(i)

    dfs(n,matrix)
    return sorted_list
    
