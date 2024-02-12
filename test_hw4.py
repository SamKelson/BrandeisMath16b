import unittest
from hw4 import transpose, complex_multiply, multiply, rotate_matrix, is_positive_semidefinite

class TestMultiply(unittest.TestCase):

    def test_square_matrix(self):
        M = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        v = [1, 2, 3]
        expected = [14, 32, 50]
        self.assertEqual(multiply(M, v), expected)

    def test_rectangular_matrix(self):
        M = [[1, 2, 3],
             [4, 5, 6]]
        v = [1, 2, 3]
        expected = [14, 32]
        self.assertEqual(multiply(M, v), expected)

    def test_single_row_matrix(self):
        M = [[1, 2, 3]]
        v = [1, 2, 3]
        expected = [14]
        self.assertEqual(multiply(M, v), expected)



class TestTranspose(unittest.TestCase):

    def test_square_matrix(self):
        M = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        expected = [[1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]]
        self.assertEqual(transpose(M), expected)

    def test_rectangular_matrix(self):
        M = [[1, 2, 3],
             [4, 5, 6]]
        expected = [[1, 4],
                    [2, 5],
                    [3, 6]]
        self.assertEqual(transpose(M), expected)

    def test_single_row_matrix(self):
        M = [[1, 2, 3]]
        expected = [[1],
                    [2],
                    [3]]
        self.assertEqual(transpose(M), expected)

class TestComplexMultiply(unittest.TestCase):
    def test_complex_multiply(self):
            z1 = (2, 3)
            z2 = (4, 5)
            expected = (-7, 22)
            self.assertEqual(complex_multiply(z1, z2), expected)

            z1 = (0, 0)
            z2 = (1, 2)
            expected = (0, 0)
            self.assertEqual(complex_multiply(z1, z2), expected)

            z1 = (3, -2)
            z2 = (-1, 4)
            expected = (5, 14)
            self.assertEqual(complex_multiply(z1, z2), expected)

            z1 = (1, 3)
            z2 = (4, 11)
            expected = (-29, 23)
            self.assertEqual(complex_multiply(z1, z2), expected)

class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix(self):
            M = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
            expected = [[3, 6, 9],
                        [2, 5, 8],
                        [1, 4, 7]]
            self.assertEqual(rotate_matrix(M), expected)
    def test_rotate_matrix_again(self):
            M = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12],
                [13,14,15,16]]
            expected = [[4, 8, 12, 16],
                        [3, 7, 11, 15],
                        [2, 6, 10,14],
                        [1, 5, 9, 13]]
            self.assertEqual(rotate_matrix(M), expected)


class TestIsPositiveSemidefinite(unittest.TestCase):

    def test_positive_semidefinite_matrix(self):
        M = [[2, -3],
             [-3, 2]]
        self.assertFalse(is_positive_semidefinite(M))

    def test_not_positive_semidefinite_matrix(self):
        M = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        self.assertFalse(is_positive_semidefinite(M))
    
    def test1(self):
        M = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertTrue(is_positive_semidefinite(M))



if __name__ == '__main__':
    unittest.main()