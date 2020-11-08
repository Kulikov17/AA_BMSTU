import unittest
from main import LevenshteinDistanceMatrix
from main import LevenshteinDistanceRecursion
from main import LevenshteinDistanceRecursionMatrix
from main import DamerauLevenshteinDistanceMatrix


class TestDist(unittest.TestCase):
    @unittest.skip('tak nado')
    def setUp(self):
        self.function = None

    def test_empty(self):
        self.assertEqual(self.function('', ''), 0)
        self.assertEqual(self.function('a', ''), 1)
        self.assertEqual(self.function('', 'a'), 1)

    def test_different(self):
        # Match
        self.assertEqual(self.function('a', 'a'), 0)
        self.assertEqual(self.function('c', 'c'), 0)
        # Delete
        self.assertEqual(self.function('ab', 'a'), 1)
        self.assertEqual(self.function('op', 'o'), 1)
        # Insert
        self.assertEqual(self.function('a', 'ab'), 1)
        # Replace
        self.assertEqual(self.function('ab', 'aс'), 1)


class TestLevMatrix(TestDist):
    def setUp(self):
        self.function = LevenshteinDistanceMatrix

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestLevRec(TestDist):
    def setUp(self):
        self.function = LevenshteinDistanceRecursion

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestLevMatrixRec(TestDist):
    def setUp(self):
        self.function = LevenshteinDistanceRecursionMatrix

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestDamLevMatrix(TestDist):
    def setUp(self):
        self.function = DamerauLevenshteinDistanceMatrix

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 1)
        self.assertEqual(self.function('abc', 'cba'), 2)

def print_matrix(n,a):
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()

if __name__ == '__main__':
   # suite = unittest.TestLoader().loadTestsFromTestCase(TestLevMatrix)
   #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevRec))
   # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevMatrixRec))
   # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDamLevMatrix))

   # unittest.TextTestRunner().run(suite)
   n = int(input())
   a = [[None] * n for i in range(n)]
   x = y = k = 0
   t = 1
   for i in range(n * n):
       if k % 3 == 0:
           if 0 <= y + 1 < n and a[x][y + 1] == None:
               a[x][y] = t
               t += 1
               y += 1
           else:
               k += 1
               continue
       elif k % 3 == 1:
           if 0 <= x + 1 < n and 0 <= y - 1 < n and a[x + 1][y - 1] == None:
               a[x][y] = t
               t += 1
               x += 1
               y -= 1
           else:
               k += 1
       else:
           if 0 <= x - 1 < n and a[x - 1][y] == None:
               a[x][y] = t
               t += 1
               x -= 1
           else:
               k += 1
               continue
   for i in range(n):
       for j in range(n):
           if i > n - j - 1:
               a[i][j] = 0
   for i in range(n):
       for j in range(n):
           if a[i][j] == None:
               a[i][j] = t
   print_matrix(n, a)