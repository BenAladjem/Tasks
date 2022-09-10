import unittest
"""
    Given a fraction as a two argument tuple, will reduce that fraction
    to it simplest form.
"""
def simplify(drob):
    a, b = drob
    for i in range(a, 2, -1):
        if a % i == 0 and b % i ==0:
            a = a // i
            b = b // i
    return (a, b)

print(simplify((3, 6)))
class TestFractions(unittest.TestCase):
    def test_simplify_base(self):
        self.assertEqual((1, 1), simplify((1, 1)))

    def test_simplify_integer(self):
        self.assertEqual((1, 1), simplify((3, 3)))

    def test_simplify_simple(self):
        self.assertEqual((1, 2), simplify((2, 4)))


if __name__ == '__main__':
    unittest.main()
