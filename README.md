📘 PDF Reader to Voice (Text-to-Speech)

  A Python-based PDF to Voice Reader that converts text from PDF files into spoken audio using offline text-to-speech.

  The project is designed to be stable for long PDFs, avoiding common speech engine crashes.



🚀 Features

📄 Read text from multi-page PDF files
🔊 Convert text to speech (offline)
🧠 Handles long PDFs without freezing
📑 Page-by-page narration
🪟 File picker dialog (Tkinter)
🛠️ Simple, beginner-friendly Python code




🧰 Technologies Used
1.Python 3
2.PyPDF2 – PDF text extraction
3.pyttsx3 – Offline Text-to-Speech engine
4.Tkinter – File selection dialog


📦 Installation
1️⃣ Clone the repository
git clone https://github.com/Nishantrana1/PDF_Reader_to_Voice.git
cd PDF_Reader_to_Voice

2️⃣ Create and activate virtual environment (recommended)
python -m venv env
env\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install pyttsx3 PyPDF2

▶️ How to Run
python TXT_TO_VOICE.py


.A file dialog will open
.Select a PDF file
.The program will start reading aloud page by page



🧠 How It Works
1.User selects a PDF file
2.PyPDF2 extracts text from each page
3.Text is split into small chunks
4.pyttsx3 converts text chunks into speech
5.The TTS engine is reinitialized per page to prevent freezing



⚠️ Known Limitations
-Cannot read scanned/image-based PDFs
-Requires text-selectable PDFs
-Voice quality depends on system voice engine

👉 For scanned PDFs, OCR (Tesseract) is required.



🛡️ Stability Fix (Important)

This project avoids a known pyttsx3 issue where long narration causes the program to freeze by:

--Splitting text into chunks

--Reinitializing the speech engine for each page

This ensures smooth playback for large PDFs.