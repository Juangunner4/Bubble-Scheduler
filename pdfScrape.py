# Juan Vazquez CS 375 Financial Simulator project

""" This Python script will be used to scrape data from a pdf filed by taking in
inputs and finding that data in the PDF.
"""

import PyPDF2

from PyPDF2 import PdfFileReader

import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Opens a pdf path and extracts the text


pagesofpdf = []

scheduleofcourse = {}




def text_extractor(path):

    code = input()

    pdf = open(path, 'rb')

    pdfreader = PyPDF2.PdfFileReader(pdf)

    num_pages = pdfreader.numPages
    count = 0
    text = ""

    while count < 1: #num_pages:
        pageObj = pdfreader.getPage(count)
        count += 1
        text += pageObj.extractText()
        pagesofpdf.append(text.split('\n'))
        for words in pagesofpdf[0]:
            if code in words:
                scheduleofcourse[words] = {}
    print('dictionary', scheduleofcourse)

            
     
text_extractor('EMU-Schedule-Of-Undergraduate-Course-Offerings.pdf')
