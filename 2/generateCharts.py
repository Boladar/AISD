import plotly
from generateNumbers import generateNumbers
from linked_list import *

tab = generateNumbers(10)
ll = Linked_list()
for n in tab:
    ll.add_element(n)

ll.print_list()

ll.delete_list()

ll.print_list()