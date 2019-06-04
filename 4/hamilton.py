import random

def hamilton(next_dictionary):
    visited = [] 
    omit = []
    hamiltonFound = False
    starting_node = random.randint(0,len(next_dictionary)-1)
    current_node = starting_node

    def go_back(current_node):
        print(visited)
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

    def find_next_omitted(previous):
        for node in next_dictionary[previous]:
            if node not in visited and node in omit:
                return node

        return None

    visit_node(current_node)
    while not hamiltonFound:
        next = find_next(current_node)

        if next is not None:
            current_node = visit_node(next)
        else:
            if check_for_starting_node(current_node) and len(visited) == len(next_dictionary):
                visit_node(starting_node)
                hamiltonFound = True
            else:
                if len(visited) == len(next_dictionary):
                    print("No hamilton, every node has been visited")
                    break
                else:
                    return hamilton(next_dictionary)

    #if hamiltonFound:
    #    for i in range(len(visited)):
    #        print(visited.pop())