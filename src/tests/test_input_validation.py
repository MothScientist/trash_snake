import unittest
from trash_snake.src.modules.input_validation import check_filename


class CheckFilenameTestCase(unittest.TestCase):

    def test_0(self):
        self.assertTrue(check_filename("IVXCML"))

    def test_1(self):
        self.assertTrue(check_filename("it`s wrong name"))

    def test_2(self):
        self.assertTrue(check_filename("ABC"))

    def test_3(self):
        self.assertTrue(check_filename("why_what_where"))

    def test_4(self):
        self.assertTrue(check_filename("arduino use COM port"))

    def test_5(self):
        self.assertFalse(check_filename("it`s wrong name?"))

    def test_6(self):
        self.assertFalse(check_filename("A_b CON"))

    def test_7(self):
        self.assertFalse(check_filename("PRN"))

    def test_8(self):
        self.assertFalse(check_filename("0_1_AUX"))

    def test_9(self):
        self.assertFalse(check_filename("COM1 for arduino port"))

    def test_10(self):
        self.assertFalse(check_filename("arduino use com port?"))

    def test_11(self):
        self.assertFalse(check_filename("text | school"))

    def test_12(self):
        self.assertFalse(check_filename("my homework: 01.01.1900"))

    def test_13(self):
        self.assertFalse(check_filename("name*"))

    def test_14(self):
        self.assertFalse(check_filename("yes/no"))

    def test_15(self):
        self.assertFalse(check_filename("<html>"))

    def test_16(self):
        self.assertFalse(check_filename("right >"))

    def test_17(self):
        self.assertFalse(check_filename("<< left"))

    def test_18(self):
        self.assertFalse(check_filename("\"name\""))

    def test_19(self):
        self.assertFalse(check_filename("good | bad"))

    def test_20(self):
        self.assertFalse(check_filename("1 || 2 || 3"))

    def test_invalid_length(self):
        self.assertFalse(check_filename("a" * 256 + ".txt"))

    def test_valid_filename(self):
        self.assertTrue(check_filename("valid_filename.txt"))

    def test_invalid_symbols(self):
        self.assertFalse(check_filename("filename?with/special*characters.txt"))

    def test_reserved_name(self):
        self.assertFalse(check_filename("CON.txt"))

    def test_empty_string(self):
        self.assertTrue(check_filename(""))

    def test_whitespace_string(self):
        self.assertTrue(check_filename("   "))

    def test_only_symbols(self):
        self.assertFalse(check_filename("#%^&*|"))

    def test_too_many_dots(self):
        self.assertTrue(check_filename("example.."))

    def test_leading_or_trailing_space(self):
        self.assertTrue(check_filename(" invalid.txt"))
        self.assertTrue(check_filename("invalid.txt "))

    def test_unicode_character(self):
        self.assertTrue(check_filename("документ.txt"))


if __name__ == '__main__':
    unittest.main()
