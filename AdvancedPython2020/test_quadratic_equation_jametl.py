import unittest
import quadratic_equation_jametl


class TestQuadratic(unittest.TestCase):
    def test_quadratic(self):
        self.assertEqual(quadratic_equation_jametl.quadratic(1, -7, 12), (4, 3))
        self.assertEqual(quadratic_equation_jametl.quadratic(7, 77, 8), (-0.1, -10.9))


if __name__ == '__main__':
    unittest.main()
