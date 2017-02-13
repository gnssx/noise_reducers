import unittest
from filters import median_filter, range_filter
from reactive import reactive_transduce, rprint, list_builder
from util import compose, transduce
from pprint import pprint



N = 5
D = 3

START = 0.2
END = 3.0


ins = [[0.,1.,2.,1.,3.],
       [1.,5.,7.,1.,3.],
       [2.,3.,4.,1.,0.],
       [3.,3.,3.,1.,3.],
       [10.,2.,4.,0.,0.]]






class TestMedianFiltersReactive(unittest.TestCase):
    def setUp(self):
        self.res = []
        transducer = median_filter(N, D) 
        self.target = reactive_transduce(
                          transducer=transducer,
                          target=list_builder(self.res))
        
    def runTest(self):
        print "Running Median Test"

        expected = [[0.,  1., 2.,  1., 3.],
                    [0.5, 3., 4.5, 1., 3.],
                    [1.,  3., 4.,  1., 3.],
                    [1.5, 3., 3.5, 1., 3.],
                    [2.5, 3., 4.,  1., 1.5]]
        
        for item in ins:
            self.target.send(item)
        self.assertEqual(self.res, expected)

        
    def cleanUp(self):
        self.array = []
        self.target.close()
        pass


class TestRangeFilterReactive(unittest.TestCase):
    def setUp(self):
        self.res = []
        transducer = range_filter(START, END)
        self.target = reactive_transduce(
                          transducer=transducer,
                          target=list_builder(self.res))

    def runTest(self):
        print "Running Range Test"

        expected = [[0.2, 1.0, 2.0, 1.0, 3.0],
                    [1.0, 3.0, 3.0, 1.0, 3.0],
                    [2.0, 3.0, 3.0, 1.0, 0.2],
                    [3.0, 3.0, 3.0, 1.0, 3.0],
                    [3.0, 2.0, 3.0, 0.2, 0.2]]
        
        for item in ins:
            self.target.send(item)

        self.assertEqual(self.res, expected)

    def cleanUp(self):
        self.array = []
        self.target.close()



class TestComposedFilterReactive(unittest.TestCase):
    def setUp(self):
        self.res = []
        transducer = compose(range_filter(START, END),
                             median_filter(N, D))

        self.target = reactive_transduce(
                          transducer=transducer,
                          target=list_builder(self.res))

    def runTest(self):
        print "\nRunning Composed Test"

        expected = [[0.2, 1.0, 2.0, 1.0, 3.0],
                    [0.6, 2.0, 2.5, 1.0, 3.0],
                    [1.0, 3.0, 3.0, 1.0, 3.0],
                    [1.5, 3.0, 3.0, 1.0, 3.0],
                    [2.5, 3.0, 3.0, 1.0, 1.6]]

        for item in ins:
            self.target.send(item)

        self.assertEqual(self.res, expected)

    def cleanUp(self):
        self.array = []
        self.target.close()




if __name__ == '__main__':
    unittest.main()

