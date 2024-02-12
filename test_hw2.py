import unittest
from hw2 import is_in_first_quadrant, dot, norm, largest_norm

class TestIsInFirstQuadrant(unittest.TestCase):
    def test_positive_values(self):
        vector = [2, 3]
        self.assertTrue(is_in_first_quadrant(vector))

    def test_zero_values(self):
        vector = [0, 0]
        self.assertTrue(is_in_first_quadrant(vector))

    def test_negative_values(self):
        vector = [-1, 4]
        self.assertFalse(is_in_first_quadrant(vector))

    def test_mixed_values(self):
        vector = [2, -3]
        self.assertFalse(is_in_first_quadrant(vector))

class TestIsInFirstQuadrant(unittest.TestCase):
    def test_positive_values(self):
        vector = [2, 3]
        self.assertTrue(is_in_first_quadrant(vector))

    def test_zero_values(self):
        vector = [0, 0]
        self.assertTrue(is_in_first_quadrant(vector))

    def test_negative_values(self):
        vector = [-1, 4]
        self.assertFalse(is_in_first_quadrant(vector))

    def test_mixed_values(self):
        vector = [2, -3]
        self.assertFalse(is_in_first_quadrant(vector))

class TestDot(unittest.TestCase):
    def test_positive_values(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        expected_result = 32
        self.assertEqual(dot(v1, v2), expected_result)

    def test_zero_values(self):
        v1 = [0, 0, 0]
        v2 = [1, 2, 3]
        expected_result = 0
        self.assertEqual(dot(v1, v2), expected_result)

    def test_negative_values(self):
        v1 = [-1, -2, -3]
        v2 = [4, 5, 6]
        expected_result = -32
        self.assertEqual(dot(v1, v2), expected_result)

    def test_mixed_values(self):
        v1 = [1, 2, 3]
        v2 = [-4, 5, -6]
        expected_result = -12
        self.assertEqual(dot(v1, v2), expected_result)

class TestNorm(unittest.TestCase):
    def test_positive_values(self):
        vector = [3, 4]
        expected_result = 5.0
        self.assertEqual(norm(vector), expected_result)

    def test_zero_values(self):
        vector = [0, 0, 0]
        expected_result = 0.0
        self.assertEqual(norm(vector), expected_result)

    def test_negative_values(self):
        vector = [-2, -3, -6]
        expected_result = 7.0
        self.assertEqual(norm(vector), expected_result)

    def test_mixed_values(self):
        vector = [1, -2, 2]
        expected_result = 3.0
        self.assertEqual(norm(vector), expected_result)

class TestLargestNorm(unittest.TestCase):
    def test_single_vector(self):
        vectors = [[1, 2, 3]]
        expected_result = [1, 2, 3]
        self.assertEqual(largest_norm(vectors), expected_result)

    def test_multiple_vectors(self):
        vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [7, 8, 9]
        self.assertEqual(largest_norm(vectors), expected_result)

    def test_tie_breaker(self):
        vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 8, 7]]
        expected_result = [7, 8, 9]
        self.assertEqual(largest_norm(vectors), expected_result)

if __name__ == '__main__':
    unittest.main()