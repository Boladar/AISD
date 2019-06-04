
def hamilton(next_dictionary):
    visited = [] 
    omit = []
    hamiltonFound = False

    def go_back(current_node):
        omit.append(current_node)
        previous = visited.pop()
        return previous

    def visit_node(node):
        #print("visit {}".format(node))
        visited.append(node)

    def find_next(previous):
        
        for node in next_dictionary[previous]:
            if node not in visited and node not in omit:
                return node

        for node in next_dictionary[previous]:
            if node not in visited:
                return node

        return None
    
    starting_node = 0
    current_node = starting_node
    visit_node(current_node)

    while not hamiltonFound:
        next = find_next(current_node)

        if next is not None:
            visit_node(next)
        else:
            hamiltonFound = True

        current_node = next

    for i in range(len(visited)):
        print(visited.pop())