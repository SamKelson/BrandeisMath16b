import unittest
from hw3 import is_scalar_multiple, reverse_dictionary, count_vectors, normalize, orthogonal_projection

class TestIsScalarMultiple(unittest.TestCase):
    def test_hw_1(self):
        self.assertTrue(is_scalar_multiple([0], [1]))
    def test_hw_2(self):
        self.assertTrue(is_scalar_multiple([0,1], [0,0]))
    def test_hw_3(self):
        self.assertTrue(is_scalar_multiple([0,0], [1,1]))
    def test_same_vectors(self):
        v1 = [1, 2, 3]
        v2 = [1, 2, 3]
        self.assertTrue(is_scalar_multiple(v1, v2))

    def test_zero_vectors(self):
        v1 = [0, 0, 0]
        v2 = [0, 0, 0]
        self.assertTrue(is_scalar_multiple(v1, v2))

    def test_scalar_multiple(self):
        v1 = [1, 2, 3]
        v2 = [2, 4, 6]
        self.assertTrue(is_scalar_multiple(v1, v2))

    def test_not_scalar_multiple(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        self.assertFalse(is_scalar_multiple(v1, v2))

    def test_not_scalar_multiple_again(self):
        v1 = [1, 2, 3]
        v2 = [4, 0, 6]
        self.assertFalse(is_scalar_multiple(v1, v2))

    def test_different_lengths(self):
        v1 = [1, 2, 3]
        v2 = [1, 2]
        self.assertFalse(is_scalar_multiple(v1, v2))

class TestReverseDictionary(unittest.TestCase):
    def test_empty_dictionary(self):
        d = {}
        expected = {}
        self.assertEqual(reverse_dictionary(d), expected)

    def test_single_value(self):
        d = {1: 'a'}
        expected = {'a': [1]}
        self.assertEqual(reverse_dictionary(d), expected)

    def test_multiple_values(self):
        d = {1: 'a', 2: 'b', 3: 'b'}
        expected = {'a': [1], 'b': [2, 3]}
        self.assertEqual(reverse_dictionary(d), expected)

    def test_duplicate_values(self):
        d = {1: 'a', 2: 'b', 3: 'b', 4: 'a'}
        expected = {'a': [1, 4], 'b': [2, 3]}
        self.assertEqual(reverse_dictionary(d), expected)

    def test_mixed_types(self):
        d = {1: 'a', 2: 2, 3: 'b', 4: 2}
        expected = {'a': [1], 2: [2, 4], 'b': [3]}
        self.assertEqual(reverse_dictionary(d), expected)

class TestCountVectors(unittest.TestCase):
    def test_empty_vectors(self):
        vectors = []
        expected = {}
        self.assertEqual(count_vectors(vectors), expected)

    def test_single_vector(self):
        vectors = [(1, 2, 3)]
        expected = {(1, 2, 3): 1}
        self.assertEqual(count_vectors(vectors), expected)

    def test_multiple_vectors(self):
        vectors = [(1, 2, 3), (1, 2, 3), (2, 3, 4), (0, 0, 0), (0,)]
        expected = {(1, 2, 3): 2, (2, 3, 4): 1, (0, 0, 0): 1, (0,): 1}
        self.assertEqual(count_vectors(vectors), expected)

    def test_duplicate_vectors(self):
        vectors = [(1, 2, 3), (1, 2, 3), (2, 3, 4), (1, 2, 3)]
        expected = {(1, 2, 3): 3, (2, 3, 4): 1}
        self.assertEqual(count_vectors(vectors), expected)

class TestNormalize(unittest.TestCase):
    def test_nonzero_vector(self):
        v = [3, 4]
        expected = [0.6, 0.8]
        self.assertEqual(normalize(v), expected)

    def test_zero_vector(self):
        v = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(normalize(v), expected)

    def already_normed(self):
        v = [3/5, 4/5]
        expected = [3/5, 4/5]
        self.assertEqual(normalize(v), expected)

    def test_negative_vector(self):
        v = [-2, -3, -4]
        expected = [-0.3713906763541037, -0.5570860145311556, -0.7427813527082074]
        self.assertEqual(normalize(v), expected)

    def test_mixed_vector(self):
        v = [1, -2, 3, -4]
        expected = [0.18257418583505536, -0.3651483716701107, 0.5477225575051661, -0.7302967433402214]
        self.assertEqual(normalize(v), expected)

class TestOrthogonalProjection(unittest.TestCase):
    def test_projection_same_direction(self):
        v = [1, 2, 3]
        w = [2, 4, 6]
        expected_x = [1, 2, 3]
        expected_y = [0, 0, 0]
        x, y = orthogonal_projection(v, w)
        self.assertEqual(x, expected_x)
        self.assertEqual(y, expected_y)

    def test_projection_different_direction(self):
        v = [1, 2, 3]
        w = [4, 5, 6]
        expected_x = [128/77, 160/77, 192/77]
        expected_y = [1-128/77, 2-160/77, 3-192/77]
        x, y = orthogonal_projection(v, w)
        map(lambda x, y: self.assertAlmostEqual(x,y), expected_x, expected_y)

    def test_projection_mixed_direction(self):
        v = [1, 2, 3]
        w = [4, 0, 6]
        expected_x = [0.4, 0, 0.6]
        expected_y = [0.6, 2, 2.4]
        x, y = orthogonal_projection(v, w)
        map(lambda x, y: self.assertAlmostEqual(x,y), expected_x, expected_y)

    def test_projection_zero_vector(self):
        v = [0, 0, 0]
        w = [1, 2, 3]
        expected_x = [0, 0, 0]
        expected_y = [0, 0, 0]
        x, y = orthogonal_projection(v, w)
        map(lambda x, y: self.assertAlmostEqual(x,y), expected_x, expected_y)

if __name__ == '__main__':
    unittest.main()