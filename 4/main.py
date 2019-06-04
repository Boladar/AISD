import generate
import euler
import hamilton

next_dictionary = generate.generate_graph(100,0.3)
#euler.euler(next_dictionary)
generate.print_list_of_next_elements(next_dictionary)
hamilton.hamilton(next_dictionary)