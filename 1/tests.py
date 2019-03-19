import unittest

import generate as g

from heapSort import heapSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from shellSort import shellSort
from quickSort import quicksort_right, quicksort_random

TEST_FUNC = [quicksort_right,quicksort_random,heapSort,insertionSort,selectionSort,shellSort]

class TestSort(unittest.TestCase):
    def test_sorts(self):
        data = g.generate_tests([g.randomised],100)
        for f in TEST_FUNC:
            for d in data:
                self.assertListEqual(f(d),sorted(d), "sort {}".format(f.__name__))
                
if __name__ == '__main__':
    unittest.main()