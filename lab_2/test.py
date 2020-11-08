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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLevMatrix)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevRec))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevMatrixRec))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDamLevMatrix))

    unittest.TextTestRunner().run(suite)
