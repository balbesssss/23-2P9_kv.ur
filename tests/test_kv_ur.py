"""Module for all unittests
"""
import unittest
from main import kv_ur


class TestsKvUr(unittest.TestCase):
    """Class for unittests
    """
    def test_more_zero(self):
        """Test for discriminant more than zero
        """
        a = 2
        b = 4
        c = -6
        d = 64
        x1 = 1
        x2 = -3
        string = "Дискриминант больше нуля, два корня"
        count = 4
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), count, "incorrect count of values")
        self.assertEqual(output[0], string, "incorrect string")
        self.assertEqual(output[1], d, "incorrect discriminant")
        self.assertEqual(output[2], x1, "incorrect x1")
        self.assertEqual(output[3], x2, "incorrect x2")

    def test_discriminant_is_zero(self):
        """Тесты для дискриминанта равная нулю"""
        a = 3
        b = -18
        c = 27
        d = 0
        x = 3
        string = "Дискриминант равен нулю, один корень"
        z = 3
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), z, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорректна")
        self.assertEqual(output[1], d, "Дискриминант некорректен")
        self.assertEqual(output[2], x, "Корень некорректен")
