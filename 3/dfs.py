from generate import Edge

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
    

def dfs_edge_list(n,edge_list):

    edge_set = set()
    for edge in edge_list:
        edge_set.add(edge)

    visited = set()
    sorted_list = []

    def visit_node(node):
        #print("true node {}".format(str(node)))
        visited.add(node)
        
        for i in range(n):
            target = Edge(node,i)
            if target in edge_set and i not in visited:
                visit_node(i)
        sorted_list.insert(0,node)

    def dfs(n,edge_list):
        for i in range(n):
            edge = edge_list[i]
            if edge[0] not in visited:
                visit_node(edge[0])

    dfs(n,edge_list)
    return sorted_list

def dfs_list_of_next_elements(n,list_of_next_elements):
    
    visited = [False for i in range(n)]
    sorted_list = []

    def visit_node(node):
        visited[node] = True

        adjacent = list_of_next_elements[node]
        for i in adjacent:
            if not visited[i]:
                visit_node(i)
        sorted_list.insert(0,node)

    def dfs(n,list_of_next_elements):
        for key in list_of_next_elements:
            if not visited[key]:
                visit_node(key)

    dfs(n,list_of_next_elements)
    return sorted_list