import unittest
from TextCount import *

class TestCalc(unittest.TestCase):

    def test_Task2(self):
        # List Of Strings
        listOfStrings = ['za','az','hi', 'hello','frim','at', 'this','za','there', 'from','aa','ha']
        self.assertEqual(wordSort(listOfStrings),sorted(listOfStrings))

    def test_Task3(self):
        listOfStrings = ['hi', 'hello', 'at', 'this', 'there', 'from']
        expecresult = [6,['at',1],['from',1],['hello',1,],['hi',1],['there',1],['this',1]]
        self.assertEqual(wordCount(wordSort(listOfStrings)),expecresult)
        anotherlist = ['za', 'az', 'hi', 'hello', 'frim', 'at','a','this', 'za', 'there', 'from', 'aa', 'ha']
        expec = [13,['a',1],['aa',1],['at',1],['az',1],['frim',1],['from',1],['ha',1],['hello',1,],['hi',1],['there',1],['this',1],['za',2]]
        self.assertEqual(wordCount(wordSort(anotherlist)), expec)

    def test_Task4(self):
        alist = [6, ['at', 1], ['from', 1], ['hello', 1 ], ['hi', 1], ['there', 1], ['this', 1]]
        k = 1
        self.assertEqual(kTopWords(k,alist[1:]),alist[1:k+1])
        k = 2
        self.assertEqual(kTopWords(k,alist[1:]),alist[1:k+1])
        k = 3
        self.assertEqual(kTopWords(k, alist[1:]), alist[1:k + 1])
        k = 4
        self.assertEqual(kTopWords(k,alist[1:]),alist[1:k+1])
        k = 5
        self.assertEqual(kTopWords(k,alist[1:]),alist[1:k+1])
        k = 6
        self.assertEqual(kTopWords(k,alist[1:]),alist[1:k+1])

        news = [11, ['aa', 3], ['at', 1],['az', 1],['from', 1],['ha', 3], ['hello', 1, ], ['hi', 1],['there', 1], ['this', 1], ['za', 2],['frim', 1]]
        exepec = [['aa', 3],['ha', 3],['za', 2],['at', 1], ['az', 1],['from', 1],['hello', 1,], ['hi', 1],['there', 1], ['this', 1],['frim', 1]]
        k = news[0]
        self.assertEqual(kTopWords(k,news[1:]),exepec)
        exepec = [['aa', 3], ['ha', 3], ['za', 2], ['at', 1], ['az', 1], ['from', 1], ['hello', 1, ], ['hi', 1]]
        k = news[0] - 3
        self.assertEqual(kTopWords(k, news[1:]), exepec)
        exepec = [['aa', 3], ['ha', 3], ['za', 2], ['at', 1]]
        k = news[0] - 7
        self.assertEqual(kTopWords(k, news[1:]), exepec)


if __name__ == '__main__':
    unittest.main()