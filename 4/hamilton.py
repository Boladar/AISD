
def hamilton(next_dictionary):
    visited = [] 
    omit = []
    hamiltonFound = False
    starting_node = 0
    current_node = starting_node

    def go_back(current_node):
        omit.append(current_node)
        previous = visited.pop()
        return previous

    def visit_node(node):
        #print("visit {}".format(node))
        visited.append(node)

        return node

    def check_for_starting_node(previous):
        for node in next_dictionary[previous]:
            if node == starting_node:
                return True

        return False


    def find_next(previous):
        
        for node in next_dictionary[previous]:
            if node not in visited and node not in omit:
                return node

        for node in next_dictionary[previous]:
            if node not in visited:
                return node

        return None

    visit_node(current_node)
    while not hamiltonFound:
        next = find_next(current_node)

        if next is not None:
            current_node = visit_node(next)
        else:
            if check_for_starting_node(current_node):
                visit_node(starting_node)
                hamiltonFound = True
            else:
                current_node = go_back(current_node)

    for i in range(len(visited)):
        print(visited.pop())