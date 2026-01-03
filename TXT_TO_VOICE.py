import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename

def split_text(text, chunk_size=800):
    for i in range(0, len(text), chunk_size):
        yield text[i:i+chunk_size]

root = tk.Tk()
root.withdraw()

book = askopenfilename(filetypes=[("PDF files", "*.pdf")])

with open(book, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    engine = pyttsx3.init()

    for page_no, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text:
            continue

        print(f"Reading page {page_no}")

        for chunk in split_text(text):
            engine.say(chunk)
            engine.runAndWait()
