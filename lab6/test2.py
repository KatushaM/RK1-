import unittest
import random
from test1 import gen_random
from test1 import format_output 

class TestGenRandom(unittest.TestCase): # TDD style

    def test_positive_count(self):
        self.assertEqual(len(gen_random(5, 1, 10)), 5)

    def test_zero_count(self):
        self.assertEqual(gen_random(0, 1, 10), [])

    def test_negative_count(self):
        self.assertEqual(gen_random(-5, 1, 10), [])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            gen_random(5, 10, 1)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            gen_random(5.5, 1, 10)


class TestGenRandomBDD(unittest.TestCase): # BDD style 

    def test_generate_five_numbers_between_one_and_ten(self):
        num_count = 5
        begin = 1
        end = 10
        result = gen_random(num_count, begin, end)
        self.assertEqual(len(result), num_count)
        self.assertTrue(all(1 <= num <= 10 for num in result))

    def test_generate_numbers_within_range(self):
        num_count = 3
        begin = 50
        end = 100
        result = gen_random(num_count, begin, end)
        self.assertEqual(len(result), num_count)
        self.assertTrue(all(50 <= num <= 100 for num in result))

    def test_handle_zero_count(self):
        num_count = 0
        begin = 1
        end = 100
        result = gen_random(num_count, begin, end)
        self.assertEqual(result, [])


class TestFormatOutput(unittest.TestCase):
    def test_format_output(self):
        self.assertEqual(format_output([1,2,3]), "1, 2, 3")
        self.assertEqual(format_output([]), "")


if __name__ == "__main__":
    unittest.main()
