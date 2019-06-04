import generate
from hamilton import hamilton

ts = 90

next_dictionary = None
while next_dictionary is None:
    next_dictionary = generate.generate_graph(ts,0.5)

while len(next_dictionary[ts-1]) > 1:
    value_to_remove = next_dictionary[ts-1].pop()
    next_dictionary[value_to_remove].remove(ts-1)


generate.print_list_of_next_elements(next_dictionary)
hamilton(next_dictionary)