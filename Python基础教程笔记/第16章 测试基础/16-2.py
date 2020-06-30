# 一个使用框架unittest的简单测试
import unittest, my_math1


class ProductTestCase(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math1.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math1.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')


if __name__ == '__main__':
    unittest.main()
