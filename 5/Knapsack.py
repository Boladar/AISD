from itertools import combinations

def dynamic_knapsack (C,n,all):
    dynamic_array = []
    x = []
    for i in range(n + 1):
        tab = [0 for i in range(C + 1)]
        dynamic_array.append(tab)

    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if all[i - 1][1] > j:
                dynamic_array[i][j] = dynamic_array[i - 1][j]
            elif all[i - 1][1] <= j:
                dynamic_array[i][j] = max(dynamic_array[i - 1][j], dynamic_array[i - 1][j - all[i - 1][1]] + all[i - 1][0])
    i = n
    j = C
    while i > 0 and j > 0:
        if dynamic_array[i][j] != dynamic_array[i - 1][j]:
            x.append(all[i-1])
            i = i - 1
            j = j - all[i][1]
        else:
            i = i - 1
    return dynamic_array[n][C],x

def bruce_force_knapsack(C,n,all):
    best_val = 0
    items = []
    for i in range(1,n+1):
        combination = list(combinations(all,i))
        for j in combination:
            tmp1 = sum([ j[x][0] for x in range(i) ])
            if tmp1 > best_val and sum([ j[x][1] for x in range(i) ]) <= C:
                items = j
                best_val = tmp1
    return best_val, items
