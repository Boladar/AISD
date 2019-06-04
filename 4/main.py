import generate
import euler

next_dictionary = generate.generate_graph(10,0.3)
euler.euler(next_dictionary)