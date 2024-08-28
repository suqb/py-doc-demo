import pytesseract
from PIL import Image
import openpyxl
import os


# 图片到文字的转换
def image_to_text(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)


# 将文字写入 Excel
def text_to_excel(origin_data, out_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    lines = origin_data.split('\n')
    for row_num, line in enumerate(lines, 1):
        sheet.cell(row=row_num, column=1, value=line)
    workbook.save(out_path)


# pytesseract.pytesseract.tesseract_cmd = r'D:/TessoractOCR/tesseract.exe'

os.environ['TESSDATA_PREFIX'] = 'D:/TesseractOCR/tessdata/'

# 使用示例
# image_path = '../image/data-image.png'
image_path = 'F:/workspace/python/doc_demo/image/excel.png'
excel_path = 'indentify-data.xlsx'
text = image_to_text(image_path)
print(text)
# text_to_excel(text, excel_path)
