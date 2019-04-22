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
