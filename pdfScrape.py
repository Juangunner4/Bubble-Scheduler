# Juan Vazquez CS 375 Financial Simulator project

""" This Python script will be used to scrape data from a pdf filed by taking in
inputs and finding that data in the PDF.
"""

import PyPDF2

from PyPDF2 import PdfFileReader

import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def text_extractor(path):  # Opens a pdf path and extracts the text with some exclusions

    pagesofpdf = []

    pdf = open(path, 'rb')

    pdfreader = PyPDF2.PdfFileReader(pdf)

    num_pages = pdfreader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfreader.getPage(count)
        count += 1
        text += pageObj.extractText()
        pagesofpdf.append(text.split('\n'))
        page = pagesofpdf[count-1]
        
        for j, line in enumerate(page):
            if '$' in line:
                page.remove(line)
            if '*' in line:
                page.remove(line)
            if len(line) == 2:
                page.remove(line)
            if len(line) == 5 and line[-1].isdigit():
                page.remove(line)
    return page

def Codefinder():

    
    pages = text_extractor('EMU-Schedule-Of-Undergraduate-Course-Offerings.pdf')
    

    code = input('Code of the course')

    for i, line in enumerate(pages):

        if code in line and line[5:8].isdigit():
            print(line)
            print(pages[i-1])

Codefinder()
