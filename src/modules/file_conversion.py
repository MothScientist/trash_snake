from PyPDF2 import PdfReader
import docx
from pathlib import Path
# from gtts import gTTS
from PIL import Image
# from os import remove
import logging

# from memory_profiler import profile
# import sys

logging.basicConfig(level=logging.DEBUG,
                    filename=f"{__name__}.log",
                    filemode='a',
                    format="%(filename)s - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
                    )

logging.getLogger("matplotlib.font_manager").disabled = True  # To suppress log-trash from matplotlib
logging.getLogger("matplotlib.pyplot").disabled = True
logging.getLogger("Image.py").disabled = True


def pdf_to_txt(pdf_path):
    logging.info("Module launched: file_conversion.pdf_to_txt")
    if Path(pdf_path).is_absolute() and Path(pdf_path).is_file() and Path(pdf_path).suffix == '.pdf':
        reader = PdfReader(pdf_path)
        outfile = open(Path(pdf_path).with_suffix('.txt'), 'w')
        for i in range(0, len(reader.pages)):
            page = reader.pages[i]
            outfile.write(page.extract_text())
        outfile.close()
    else:
        raise FileNotFoundError('[Error] The path is incorrect!')


# def pdf_to_mp3(pdf_path):
#     pdf_to_txt(pdf_path)
#     txt_path = Path(pdf_path).with_suffix('.txt')
#     audio_decode = gTTS(Path(txt_path).read_text())
#     mp3_path = Path(pdf_path).with_suffix('.mp3')
#     audio_decode.save(mp3_path)
#     remove(txt_path)  # delete txt file after converting pdf -> txt -> mp3


# def txt_to_mp3(txt_path):
#     if Path(txt_path).is_absolute() and Path(txt_path).is_file() and Path(txt_path).suffix == '.txt':
#         readfile = Path(txt_path)
#         audio_decode = gTTS(readfile.read_text())
#         audio_decode.save(Path(txt_path).with_suffix('.mp3'))
#     else:
#         raise FileNotFoundError('[Error] The path is incorrect!')


def jpeg_to_ico(jpeg_path):
    logging.info("Module launched: file_conversion.jpeg_to_ico")
    if Path(jpeg_path).is_absolute() and Path(jpeg_path).is_file() and Path(jpeg_path).suffix == '.jpeg':
        filename = jpeg_path
        img = Image.open(filename)
        img.save(Path(jpeg_path).with_suffix('.ico'))
    else:
        raise FileNotFoundError('[Error] The path is incorrect!')


def png_to_ico(png_path):
    logging.info("Module launched: file_conversion.png_to_ico")
    if Path(png_path).is_absolute() and Path(png_path).is_file() and Path(png_path).suffix == '.png':
        img = Image.open(png_path)
        ico_path = Path(png_path).with_suffix('.ico')
        img.save(ico_path)
    else:
        raise FileNotFoundError('[Error] The path is incorrect!')


def docx_to_txt(docx_file):
    logging.info("Module launched: file_conversion.docx_to_txt")
    try:
        if Path(docx_file).is_absolute() and Path(docx_file).is_file() and Path(docx_file).suffix == '.docx':
            doc = docx.Document(docx_file)
            with open(Path(docx_file).with_suffix('.txt'), 'w',
                      encoding='utf-8') as output:
                for paragraph in doc.paragraphs:
                    output.write(paragraph.text + "\n")
        else:
            raise FileNotFoundError('[Error] The path is incorrect!')
    except docx.opc.exceptions.PackageNotFoundError as docx_except:
        logging.error(docx_except)
        raise FileNotFoundError
