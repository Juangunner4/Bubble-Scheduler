# Juan Vazquez CS 375 Financial Simulator project

""" This Python script will be used to scrape data from a pdf filed by taking in
inputs and finding that data in the PDF.
"""

import PyPDF2

pdfFile = open('EMU-Schedule-Of-Undergraduate-Course-Offerings.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)
