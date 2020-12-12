import unittest

import main

class MyTestCase(unittest.TestCase):
    """Test case for function in main.py for day04 of advent of code 2020"""

    def test_byr(self) :
        self.assertEqual(main.check_byr("2000"), 1)
        self.assertEqual(main.check_byr("2020"), 0)
        self.assertEqual(main.check_byr("200"), 0)

    def test_iyr(self) :
        self.assertEqual(main.check_iyr("2015"), 1)
        self.assertEqual(main.check_iyr("2000"), 0)
        self.assertEqual(main.check_iyr("200"), 0)

    def test_eyr(self) :
        self.assertEqual(main.check_eyr("2025"), 1)
        self.assertEqual(main.check_eyr("2010"), 0)
        self.assertEqual(main.check_eyr("200"), 0)

    def test_hgt(self) :
        self.assertEqual(main.check_hgt("160cm"), 1)
        self.assertEqual(main.check_hgt("65in"), 1)
        self.assertEqual(main.check_hgt("145cm"), 0)
        self.assertEqual(main.check_hgt("80in"), 0)
        self.assertEqual(main.check_hgt("6ft"), 0)

    def test_hcl(self) :
        self.assertEqual(main.check_hcl("#123abc"), 1)
        self.assertEqual(main.check_hcl("#123xyz"), 0)
        self.assertEqual(main.check_hcl("#123"), 0)
        self.assertEqual(main.check_hcl("123abc"), 0)

    def test_ecl(self) :
        self.assertEqual(main.check_ecl("brn"), 1)
        self.assertEqual(main.check_ecl("xyz"), 0)

    def test_pid(self) :
        self.assertEqual(main.check_pid("012345678"), 1)
        self.assertEqual(main.check_pid("123456789"), 1)
        self.assertEqual(main.check_pid("0123456789"), 0)
        self.assertEqual(main.check_pid("01234567"), 0)
        self.assertEqual(main.check_pid("0123ab678"), 0)


if __name__ == '__main__':
    unittest.main()
