import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename

def split_text(text, size=600):
    for i in range(0, len(text), size):
        yield text[i:i+size]

root = tk.Tk()
root.withdraw()

book = askopenfilename(filetypes=[("PDF files", "*.pdf")])

with open(book, "rb") as f:
    reader = PyPDF2.PdfReader(f)

    for page_no, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text or not text.strip():
            continue

        print(f"Reading page {page_no}")

        # 🔥 REINITIALIZE engine per page
        engine = pyttsx3.init()
        engine.setProperty("rate", 160)

        for chunk in split_text(text):
            engine.say(chunk)

        engine.runAndWait()
        engine.stop()
