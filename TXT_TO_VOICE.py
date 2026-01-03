import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename

# create hidden Tk window
root = tk.Tk()
root.withdraw()

# select PDF
book = askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])

if not book:
    print("No file selected")
    exit()

# open PDF
with open(book, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pages = len(pdf_reader.pages)

    # initialize text-to-speech engine ONCE
    engine = pyttsx3.init()

    for num in range(pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()

        if text:  # avoid empty pages
            engine.say(text)

    engine.runAndWait()
