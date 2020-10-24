import os

import PyPDF2


"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path: str):
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    return text



base = 'sociedades-pdf'
files = os.listdir('./%s' % base)
for file in files:
    file_path = './%s/%s' % (base, file)
    print(file_path)
    print(pdf_to_text(file_path))


# # el bonus
# base = 'sociedades-b-pdf'
# files = os.listdir('./%s' % base)
# for file in files:
#     file_path = './%s/%s' % (base, file)
#     print(file_path)
#     print(pdf_to_text(file_path))