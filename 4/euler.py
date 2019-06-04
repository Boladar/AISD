import generate

def euler(next_dictionary):

    visited = []
    omit = []
    path = []

    def isBridge(next):
        deg = len(next_dictionary[next])
        if deg > 1:
            return False
        else:
            return True

    def find_next(node):
        for connection in next_dictionary[node]:
            if not isBridge(connection) and connection not in omit:
                return connection

        for connection in next_dictionary[node]:
            if connection not in omit:
                return connection

        for connection in next_dictionary[node]:
            return connection

        return None

    def calculate_number_of_edges():
        sum = 0
        for key in next_dictionary:
            sum += len(next_dictionary[key])
        return sum

    def visit_node(previous, current):
        
        next_dictionary[previous].remove(current)
        next_dictionary[current].remove(previous)

        return current

    def go_back(current):
        previous = visited.pop()
        omit.append(current)
        return previous

    current_node = 0
    while calculate_number_of_edges() > 0:
        next = find_next(current_node)

        if next is None:
            current_node = go_back(current_node)
        else:
            visited.append(current_node)
            current_node = visit_node(current_node,next)

    visited.append(current_node)

    for i in range(len(visited)):
        print(visited.pop())