import pyttsx3
import PyPDF2

from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

# Specify file type (PDF file type)
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
print(root.filename)
pdfFile = root.filename

# Assign the selected PDF file to the variable, book
book = open(str(pdfFile), 'rb')

# pdfRead assigned to the task of PdfFileReader
pdfRead = PyPDF2.PdfFileReader(book)

# This line finds the total number of pages the selected PDF file has
totalPages = pdfRead.numPages
print('The total number of pages in the PDF you selected is: ' + str(totalPages))

speaker = pyttsx3.init()

# Assign bPage page number of .pdf you want to read
print('Please enter the page number would you like the reader to begin reading from: ')
whatPage = input()
inputPage = int(whatPage) - 1

for i in range(inputPage, totalPages, 1):
    print('Now reading page: ' + str(i + 1))
    bPage = pdfRead.getPage(i)
    text = bPage.extractText()
    speaker.say(text)
    speaker.runAndWait()