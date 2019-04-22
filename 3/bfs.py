def bfs_adj_m(size,matrix):
    queue=[0]*size
    tlist=[]
    for i in range(size):
        for j in range(size):
            if matrix[j][i]==1:
                queue[i]+=1
    i=0
    while i<len(queue):
        if queue[i]==0:
            tlist.append(i)
            queue[i]-=1
            for j in range(size):
                if matrix[i][j]==1:
                    queue[j]-=1
            i=0
        else:
            i+=1
    return tlist


def bfs_edg_l(size,edglist):
    queue=[0]*size
    tlist=[]
    for i in range(len(edglist)):
            queue[edglist[i][1]]+=1
    i=0
    while i<len(queue):
        if queue[i]==0:
            tlist.append(i)
            queue[i]-=1
            for j in range(len(edglist)):
                if edglist[j][0]==i:
                    queue[edglist[j][1]]-=1
            i=0
        else:
            i+=1
    return tlist


def bfs_nxt_e(size,nxtlist):
    queue=[0]*size
    tlist=[]
    for v in nxtlist.values():
        for i in v:
            queue[i]+=1
    i=0
    while i<len(queue):
        if queue[i]==0:
            tlist.append(i)
            queue[i]-=1
            for j in nxtlist.get(i):
                queue[j]-=1
            i=0
        else:
            i+=1
    return tlist

#graph=[[0,1,0,1,1,0,0,0],
#        [0,0,1,0,0,1,0,0],
#        [0,0,0,0,1,0,0,0],
#        [0,0,0,0,1,0,0,0],
#        [0,0,0,0,0,1,0,1],
#        [0,0,0,0,0,0,0,1],
#        [0,0,0,0,1,0,0,1],
#        [0,0,0,0,0,0,0,0]]))
#print(bfs_adj_m(8,graph))
#graph=[[0,1],[0,4],[0,3],[1,2],[1,5],[2,4],[3,4],[4,5],[4,7],[5,7],[6,4],[6,7]]
#print(bfs_edg_l(8,graph))
#graph={0:[1,3,4],1:[2,5],2:[4,5],3:[4],4:[5,7],5:[7],6:[4,7],7:[]}
#print(bfs_nxt_e(8,graph))
