import unittest
from trash_snake.src.modules.search_engine import sort_files_extensions


class SortFilesExtensionsTestCase(unittest.TestCase):

    def test_0(self):
        var = sort_files_extensions(["H:\\Users\\UserName\\Downloads\\file11.txt",
                                     "H:\\Users\\UserName\\Downloads\\file11.pdf", "C:\\Windows\\file15.txt",
                                     "C:\\Games\\file16.txt", "C:\\AppData\\file17.txt",
                                     "C:\\UserProfile\\wrong_file.ini", "C:\\Users\\UserName\\Links\\file26.log"])
        var_txt = var[0]
        var_doc = var[1]
        var_pdf = var[2]
        self.assertEqual(len(var_txt), 5)
        self.assertEqual(len(var_doc), 0)
        self.assertEqual(len(var_pdf), 1)

    def test_1(self):
        var = sort_files_extensions([])
        var_txt = var[0]
        var_doc = var[1]
        var_pdf = var[2]
        self.assertEqual(len(var_txt), 0)
        self.assertEqual(len(var_doc), 0)
        self.assertEqual(len(var_pdf), 0)

    def test_2(self):
        var = sort_files_extensions(["   "])
        var_txt = var[0]
        var_doc = var[1]
        var_pdf = var[2]
        self.assertEqual(len(var_txt), 0)
        self.assertEqual(len(var_doc), 0)
        self.assertEqual(len(var_pdf), 0)


if __name__ == '__main__':
    unittest.main()
