import plotly.plotly
import plotly.graph_objs as go
import time
import sys

import generate

import bfs
import dfs


sys.setrecursionlimit(100000000)

def print_adjacency_matrix(n,graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print("")
'''

'''

def test_func(func,data,size):
    print("func: {}, size: {}".format(func.__name__,s))
    start = time.time()
    func(size,data.copy())
    end = time.time()

    return end-start

TEST_SIZES = [200,400,600,800,1000,1200,1400,1600,1800,2000]
#TEST_SIZES = [200,400]

dfs_func_traces = []
bfs_func_traces = []

timesd = []
timesb = []
for s in TEST_SIZES:
    adjacency_matrix = generate.generate_adjacency_matrix(s)        
    timesd.append(test_func(dfs.dfs_adjacency_matrix,adjacency_matrix,s))
    timesb.append(test_func(bfs.bfs_adj_m,adjacency_matrix,s))

dfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesd,mode = 'lines', name=dfs.dfs_adjacency_matrix.__name__))
bfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesb,mode = 'lines', name=bfs.bfs_adj_m.__name__))

timesd = []
timesb = []
for s in TEST_SIZES:
    adjacency_matrix = generate.generate_adjacency_matrix(s)
    edge_list = generate.generate_edge_list(s,adjacency_matrix)        
    timesd.append(test_func(dfs.dfs_edge_list,edge_list,s))
    timesb.append(test_func(bfs.bfs_edg_l,edge_list,s))

dfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesd,mode = 'lines', name=dfs.dfs_edge_list.__name__))
bfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesb,mode = 'lines', name=bfs.bfs_edg_l.__name__))

timesd = []
timesb = []
for s in TEST_SIZES:
    adjacency_matrix = generate.generate_adjacency_matrix(s)        
    next_element = generate.generate_list_of_next_elements(s,adjacency_matrix)
    timesd.append(test_func(dfs.dfs_list_of_next_elements,next_element,s))
    timesb.append(test_func(bfs.bfs_nxt_e,next_element,s))

dfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesd,mode = 'lines', name=dfs.dfs_list_of_next_elements.__name__))
bfs_func_traces.append(go.Scatter(x = TEST_SIZES,y = timesb,mode = 'lines', name=bfs.bfs_nxt_e.__name__))


plotly.offline.plot(dfs_func_traces,filename="charts/{}.html".format("dfs"))
plotly.offline.plot(bfs_func_traces,filename="charts/{}.html".format("bfs"))
plotly.offline.plot(dfs_func_traces + bfs_func_traces,filename="charts/{}.html".format("all"))