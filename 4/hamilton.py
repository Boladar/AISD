
def hamilton(next_dictionary):
    path = list()
    starting_node = 0

    def is_valid(node):
        if node in path:
            return False
        else:
            return True

    def cycle_found(node):
        if len(path) == (len(next_dictionary)):
            if starting_node in next_dictionary[node]:
                return True
            else:
                return False
                
        for n in next_dictionary[node]:
            if is_valid(n):
                path.append(n)
                if cycle_found(n):
                    return True

                path.pop()
            
        return False

    path.append(0)
    if not cycle_found(0):
        print("there's no hamiltonian cycle")
        return None
    else:
        path[len(next_dictionary)-1] = 0
        return path