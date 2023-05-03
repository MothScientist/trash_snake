import os
import re
import logging
from PyPDF2 import PdfReader  # reading pdf-files
from docx import Document  # reading docx-files

logging.basicConfig(level=logging.DEBUG,
                    filename=f"{__name__}.log",
                    filemode='a',
                    format="%(filename)s - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
                    )
logging.getLogger('matplotlib.font_manager').disabled = True  # To suppress log-trash from matplotlib
logging.getLogger('matplotlib.pyplot').disabled = True


def search_files(directory: list, pattern: list, extension: list):
    logging.info("module launched")
    paths_empty = []
    for disk in directory:
        for direction_path, _, filenames in os.walk(disk):
            for filename in filenames:  # unpacking directories to files
                for end in extension:
                    if os.path.join(direction_path, filename).endswith(end):
                        for key in pattern:  # find files with the desired names
                            if re.search(key, filename):
                                paths_empty.append(os.path.join(direction_path, filename))
    logging.info("results -> {paths_empty}")
    return paths_empty


def sort_files_extensions(sort_path_to_file):
    logging.debug("sorting started")
    sort_txt_path, sort_doc_path, sort_pdf_path = [], [], []
    for path_sort in sort_path_to_file:
        if re.search(r'txt$', path_sort) or re.search(r'log$', path_sort):
            sort_txt_path.append(path_sort)
        elif re.search(r'doc$', path_sort) or re.search(r'docx$', path_sort) or re.search(r'DOCX$', path_sort):
            sort_doc_path.append(path_sort)
        elif re.search(r'pdf$', path_sort):
            sort_pdf_path.append(path_sort)
    logging.debug("sorting finished")
    return sort_txt_path, sort_doc_path, sort_pdf_path


class DeepSearching:
    def __init__(self, search_patterns):
        self.pattens = search_patterns

    def deep_search_txt(self, txt_paths):
        for intended_path in txt_paths:
            try:
                with open(intended_path, 'r', encoding='UTF8') as file:  # add opportunity changes encoding
                    search_indicator = True
                    for line in file:
                        if search_indicator:
                            for pattern in self.pattens:
                                if re.search(pattern, line):
                                    search_indicator = False
                                    break
                        else:
                            break
                    if search_indicator:
                        txt_paths.remove(intended_path)
            except UnicodeDecodeError:
                logging.error(f'UnicodeDecodeError -> {intended_path}')
                txt_paths.remove(intended_path)
                continue
            except FileNotFoundError:
                logging.error(f'FileNotFoundError -> {intended_path}')
                txt_paths.remove(intended_path)
                continue
        logging.info(f'Detected files with extension .txt -> {txt_paths}')
        return txt_paths

    # Add a warning to the user that it is necessary to provide for a long scan of this type of files.
    # Therefore, it`s necessary to carefully check the patterns and set page limit
    # for a faster response to a search query.
    # 2000 pages - 40s, 450 - 8s, 565 - 21s
    def deep_search_pdf(self, pdf_paths, max_size_len_return=500):  # Contains an optional parameter
        for intended_path in pdf_paths:
            try:
                pdf = PdfReader(intended_path)
                if len(pdf.pages) <= max_size_len_return:
                    # We take into account the limitation on the number of pages of a pdf file,
                    # since reading it is quite time and resource consuming.
                    # P.S. If you do not need to search inside books and textbooks, then the 500 pages limit is enough.
                    search_indicator = True
                    for page in pdf.pages:
                        if search_indicator:
                            for pattern in self.pattens:
                                if re.search(pattern, page.extract_text()):
                                    search_indicator = False
                                    # As soon as we find what interests us, we stop reading the file
                                    break
                        else:
                            break
                    if search_indicator:
                        pdf_paths.remove(intended_path)
                        # If the indicator did not work,
                        # then we did not find anything in the file, and you can delete it from the list
            except FileNotFoundError:
                logging.error(f'FileNotFoundError -> {intended_path}')
                pdf_paths.remove(intended_path)
                continue
        logging.info(f'Detected files with extension .pdf -> {pdf_paths}')
        return pdf_paths

    # 34140 words = 0.108s, 31200 words = 0.089s
    # What if .doc file have a password?
    def deep_search_docx(self, doc_paths):
        for intended_path in doc_paths:
            try:
                doc = Document(intended_path)
                search_indicator = True
                for paragraph in doc.paragraphs:
                    if search_indicator:
                        for pattern in self.pattens:
                            if re.search(pattern, paragraph.text):
                                search_indicator = False
                                break
                    else:
                        break
                if search_indicator:
                    doc_paths.remove(intended_path)
            except FileNotFoundError:
                logging.error(f'FileNotFoundError -> {intended_path}')
                doc_paths.remove(intended_path)
                continue
        logging.info(f'Detected files with extension .docx -> {doc_paths}')
        return doc_paths


# add and test: .odt, .log, .djvu
