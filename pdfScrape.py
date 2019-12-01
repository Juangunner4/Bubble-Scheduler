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


Courses = []  # Stores the Course and the Time

def Codefinder(): # Searches the PDF for the Code and adds it to the Courses list

    
    pages = text_extractor('EMU-Schedule-Of-Undergraduate-Course-Offerings.pdf')


    print('Please provide the Course Code you would like to add to your schedule\n')

    code = input('Code of the course, type quit to finish adding courses')
        
    for i, line in enumerate(pages):

        if code in line and line[5:8].isdigit():
            if line not in Courses:
                Courses.append(line)
                Courses.append(pages[i-1])
   

Codefinder()
print(Courses)

