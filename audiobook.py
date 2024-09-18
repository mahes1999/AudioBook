import PyPDF2
import pyttsx3
from tkinter import Tk, filedialog

def browse_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a PDF", filetypes=[("PDF Files", "*.pdf")])
    root.destroy()  # Destroy the root window after file dialog
    return file_path

def pdf_to_audio(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            speaker = pyttsx3.init()

            # Set the desired speaking rate (lower values for slower reading)
            speaker.setProperty('rate', 150)  # Adjust as needed

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text:  # Only speak if there's text on the page
                    speaker.say(text)
                    speaker.runAndWait()

            speaker.stop()
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    pdf_file = browse_file()
    if pdf_file:
        pdf_to_audio(pdf_file)
    else:
        print("No file selected.")