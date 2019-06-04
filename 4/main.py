import generate
import euler
import hamilton

next_dictionary = None
while next_dictionary is None:
    next_dictionary = generate.generate_graph(80,0.7)

#euler.euler(next_dictionary)
generate.print_list_of_next_elements(next_dictionary)
hamilton.hamilton(next_dictionary)