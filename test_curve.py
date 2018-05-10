import unittest
from snake_curve import snake

class TestCurveGenerator(unittest.TestCase):

    def test_2x2(self):
        snake_transform = snake(2, 2)
        self.assertEqual(snake_transform, [(0, 0), (0, 1), (1, 1), (1, 0)])


    def test_3x3(self):
        snake_transform = snake(3, 3)
        self.assertEqual(snake_transform, [
            (0, 0), (0, 1), (0, 2),
            (1, 2), (1, 1), (1, 0),
            (2, 0), (2, 1), (2, 2)
        ])

if __name__ == '__main__':
    unittest.main()
