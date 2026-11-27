#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)
        self.assertEqual(max_integer([2, 9, 1, 8, 3]), 9)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 99, 4, 3]), 99)

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 3, 4, 100]), 100)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)
        self.assertEqual(max_integer([0]), 0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)
        self.assertEqual(max_integer([-10, 0, -20]), 0)

    def test_duplicated_max(self):
        self.assertEqual(max_integer([5, 5, 1]), 5)
        self.assertEqual(max_integer([1, 5, 5]), 5)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)

    def test_integers_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)
        self.assertEqual(max_integer([3, 2.5, 1.5]), 3)

    def test_big_numbers(self):
        self.assertEqual(max_integer([10 ** 20, 1, 10 ** 19]), 10 ** 20)

    def test_infinity(self):
        self.assertEqual(max_integer([1, float('inf'), 5]), float('inf'))
        self.assertEqual(max_integer([float('-inf'), -5]), -5)

    def test_the_list_is_not_changed(self):
        numbers = [3, 1, 2]
        max_integer(numbers)
        self.assertEqual(numbers, [3, 1, 2])

    def test_tuple(self):
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string_of_characters(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_numbers_that_cannot_be_compared(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])
        with self.assertRaises(TypeError):
            max_integer([1, None])

    def test_documentation(self):
        module = __import__('6-max_integer')
        self.assertTrue(len(module.__doc__) > 1)
        self.assertTrue(len(module.max_integer.__doc__) > 1)


if __name__ == '__main__':
    unittest.main()
