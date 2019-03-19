import random

def quicksort_right(table):
    def partition(table,left, right):
        x = table[right]
        i = left - 1
        for j in range(left,right):
            if(table[j] <= x):
                i += 1
                table[i],table[j] = table[j],table[i]
        table[i+1],table[right] = table[right],table[1+i]
        return i+1

    def quicksort(table,left,right):
        if (left  < right):
            q = partition(table,left,right)
            quicksort(table,left,q-1)
            quicksort(table,q+1,right)

    quicksort(table,0,len(table)-1)
    return table

def quicksort_random(table):
    def partition(table,left,right):
        random_index = random.randint(left,right)
        table[right],table[random_index] = table[random_index],table[right]

        x = left
        for i in range(left,right):
            if (table[i] < table[right]):
                table[i],table[x] = table[x],table[i]
                x += 1
        table[x],table[right] = table[right],table[x]
        return x
    
    def quicksort(table,left,right):
        if (left  < right):
            q = partition(table,left,right)
            quicksort(table,left,q-1)
            quicksort(table,q+1,right)

    quicksort(table,0,len(table)-1)
    return table
