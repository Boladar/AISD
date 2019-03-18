import unittest

import generate as g

from heapSort import heapSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from shellSort import shellSort

TEST_FUNC = [shellSort,heapSort,insertionSort,selectionSort]

class TestSort(unittest.TestCase):
    def test_sorts(self):
        data = g.generate_tests([g.up,g.down,g.a,g.v,g.stale,g.randomised],100)
        for f in TEST_FUNC:
            self.assertListEqual(f(data[0]),sorted(data[0]))

if __name__ == '__main__':
    unittest.main()