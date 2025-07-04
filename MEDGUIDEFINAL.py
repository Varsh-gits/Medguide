##import warnings
##warnings.filterwarnings("ignore", category=UserWarning)
##import tkinter as tk
##from tkinter import filedialog, messagebox
##from PIL import Image, ImageTk
##import pytesseract
##import pandas as pd
##from deep_translator import GoogleTranslator
##from gtts import gTTS
##import os
##import tempfile
##import pygame
##import time
##
### Initialize translator and pygame
####translator = Translator()
##pygame.init()
##
### Set path to tesseract executable
##pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this if needed
##
### Get medicine details from namesfinal.csv
##def get_medicine_details(med_name):
##    try:
##        df = pd.read_csv(r"C:\Users\Varsh\Desktop\namesfinal.csv",encoding='cp1252')
##        matched = df[df.iloc[:, 0].str.lower().str.contains(med_name.lower())]
##
##        if matched.empty:
##            return None
##
##        row = matched.iloc[0]
##        details = {}
##        for col in df.columns[1:]:
##            details[col] = row[col]
##        return details
##
##    except Exception as e:
##        print(f"Error reading CSV: {e}")
##        return None
##
### Translate text
##
####def translate_text(text, lang):
####    try:
####        translated = translator.translate(text, dest=lang)
####        return translated.text
####    except:
####        return text  # Fallback to original
##def translate_text(text, lang):
##    try:
##        return GoogleTranslator(source='auto', target=lang).translate(text)
##    except:
##        return text
##
### Speak text using gTTS
##
##def speak_text(text, lang='en'):
##    try:
##        # Create a temporary mp3 file
##        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
##            tts = gTTS(text=text, lang=lang)
##            fp_path = fp.name
##            tts.save(fp_path)
##
##        # Initialize and play audio with pygame
##        pygame.mixer.init()
##        pygame.mixer.music.load(fp_path)
##        pygame.mixer.music.play()
##
##        # Wait for the audio to finish playing
##        while pygame.mixer.music.get_busy():
##            pygame.time.Clock().tick(10)
##
##        time.sleep(1)
##        os.remove(fp_path)
##
##    except Exception as e:
##        print(f"Audio error: {e}")
##
##
### Extract text from image
##
##def extract_text(image_path):
##    img = Image.open(image_path)
##    gray = img.convert('L')
##    text = pytesseract.image_to_string(gray)
##    return text.strip()
##
### Handle photo upload
##
####def upload_photo():
####    file_path = filedialog.askopenfilename()
####    if not file_path:
####        return
####
####    extracted = extract_text(file_path)
####    if not extracted.strip():
####        messagebox.showerror("Error", "No text found in the image. Please try again with a clearer photo.")
####        return
####
####    med_name = extracted.split()[0]  # crude way to pick first medicine name
####    details = get_medicine_details(med_name)
####    if not details:
####        messagebox.showerror("Error", f"No details found for '{med_name}' in namesfinal.csv")
####        return
####
####    # Clear frame and show results
####    for widget in result_frame.winfo_children():
####        widget.destroy()
####
####    tk.Label(result_frame, text=f"Medicine: {med_name}", font=("Arial", 14, "bold")).pack(pady=5)
####
####    for label, value in details.items():
####        en = f"{label}: {value}"
####        hi = translate_text(en, 'hi')
####        ta = translate_text(en, 'ta')
####
####        tk.Label(result_frame, text=en, wraplength=400, justify="left").pack(anchor='w')
####        tk.Label(result_frame, text=f"[हिंदी] {hi}", fg="green", wraplength=400, justify="left").pack(anchor='w')
####        tk.Label(result_frame, text=f"[தமிழ்] {ta}", fg="purple", wraplength=400, justify="left").pack(anchor='w')
####        tk.Button(result_frame, text="🔊 Listen (EN)", command=lambda t=en: speak_text(t, 'en')).pack(anchor='w')
####        tk.Button(result_frame, text="🔊 सुनो (HI)", command=lambda t=hi: speak_text(t, 'hi')).pack(anchor='w')
####        tk.Button(result_frame, text="🔊 கேள் (TA)", command=lambda t=ta: speak_text(t, 'ta')).pack(anchor='w')
####        tk.Label(result_frame, text="").pack()  # spacer
##
##def upload_photo():
##    file_path = filedialog.askopenfilename()
##    if not file_path:
##        return
##
##    extracted = extract_text(file_path)
##    if not extracted.strip():
##        messagebox.showerror("Error", "No text found in the image. Please try again with a clearer photo.")
##        return
##
##    med_names = extracted.split()  # Split the whole OCR text by space (crude medicine name detection)
##
##    found_any = False
##    for med_name in med_names:
##        details = get_medicine_details(med_name)
##        if not details:
##            continue  # skip if not found
##
##        found_any = True
##
##        # Show results for each medicine
##        tk.Label(result_frame, text=f"Medicine: {med_name}", font=("Arial", 14, "bold")).pack(pady=5)
##
##        for label, value in details.items():
##            en = f"{label}: {value}"
##            hi = translate_text(en, 'hi')
##            ta = translate_text(en, 'ta')
##
##            tk.Label(result_frame, text=en, wraplength=400, justify="left").pack(anchor='w')
##            tk.Label(result_frame, text=f"[हिंदी] {hi}", fg="green", wraplength=400, justify="left").pack(anchor='w')
##            tk.Label(result_frame, text=f"[தமிழ்] {ta}", fg="purple", wraplength=400, justify="left").pack(anchor='w')
##            tk.Button(result_frame, text="🔊 Listen (EN)", command=lambda t=en: speak_text(t, 'en')).pack(anchor='w')
##            tk.Button(result_frame, text="🔊 सुनो (HI)", command=lambda t=hi: speak_text(t, 'hi')).pack(anchor='w')
##            tk.Button(result_frame, text="🔊 கேள் (TA)", command=lambda t=ta: speak_text(t, 'ta')).pack(anchor='w')
##            tk.Label(result_frame, text="").pack()
##
##    if not found_any:
##        messagebox.showerror("Error", "No known medicine names found in the image.")
##
### Setup GUI
##root = tk.Tk()
##root.title("MedGuide - AI Medicine Assistant")
##root.geometry("700x700")
##root.configure(bg="lavender")
##
### Heading
##tk.Label(root, text="MedGuide - An AI Tool to Assist with Medicines", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)
##tk.Label(root, text="⚠️ It is recommended to consult doctors. Do not rely solely on MedGuide.", fg="red", bg="white").pack(pady=5)
##
### Buttons
##button_frame = tk.Frame(root, bg="white")
##button_frame.pack(pady=20)
##tk.Button(button_frame, text="📷 Take Photo", font=("Arial", 12), command=upload_photo, bg="#cceeff").pack(side="left", padx=10)
##tk.Button(button_frame, text="📁 Upload Photo", font=("Arial", 12), command=upload_photo, bg="#ccffcc").pack(side="left", padx=10)
##
### Result display
##result_frame = tk.Frame(root, bg="white")
##result_frame.pack(pady=10)
##
##root.mainloop()


######import tkinter as tk
######from tkinter import filedialog, messagebox
######from PIL import Image, ImageTk
######import pytesseract
######import pandas as pd
######from gtts import gTTS
######import os
######import tempfile
######import pygame
######
####### Initialize pygame
######pygame.init()
######
####### Set path to tesseract executable
######pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this if needed
######
######def get_medicine_details(med_name):
######    try:
######        # Try ISO-8859-1 (Latin-1), which handles many special characters
######        df = pd.read_csv(r"C:\Users\Varsh\Desktop\namesfinal.csv", encoding="ISO-8859-1")
######        matched = df[df.iloc[:, 0].str.lower().str.contains(med_name.lower())]
######
######        if matched.empty:
######            return None
######
######        row = matched.iloc[0]
######        details = {}
######        for col in df.columns[1:]:
######            details[col] = row[col]
######        return details
######
######    except Exception as e:
######        print(f"Error reading CSV: {e}")
######        return None
######
######
####### Get medicine details from namesfinal.csv
########def get_medicine_details(med_name):
########    try:
########        df = pd.read_csv(r"C:\Users\Varsh\Desktop\namesfinal.csv")
########        matched = df[df.iloc[:, 0].str.lower().str.contains(med_name.lower())]
########
########        if matched.empty:
########            return None
########
########        row = matched.iloc[0]
########        details = {}
########        for col in df.columns[1:]:
########            details[col] = row[col]
########        return details
########
########    except Exception as e:
########        print(f"Error reading CSV: {e}")
########        return None
######
####### Speak text using gTTS (English only for now)
######def speak_text(text):
######    try:
######        tts = gTTS(text=text, lang='en')
######        with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as fp:
######            tts.save(fp.name)
######            pygame.mixer.music.load(fp.name)
######            pygame.mixer.music.play()
######            while pygame.mixer.music.get_busy():
######                continue
######    except Exception as e:
######        print(f"Audio error: {e}")
######
####### Extract text from image
######def extract_text(image_path):
######    img = Image.open(image_path)
######    gray = img.convert('L')
######    text = pytesseract.image_to_string(gray)
######    return text.strip()
######
####### Handle photo upload
######def upload_photo():
######    file_path = filedialog.askopenfilename()
######    if not file_path:
######        return
######
######    extracted = extract_text(file_path)
######    if not extracted.strip():
######        messagebox.showerror("Error", "No text found in the image. Please try again with a clearer photo.")
######        return
######
######    med_names = extracted.split()
######    found_any = False
######
######    for widget in result_canvas.winfo_children():
######        widget.destroy()
######
######    for med_name in med_names:
######        details = get_medicine_details(med_name)
######        if not details:
######            continue
######
######        found_any = True
######
######        frame = tk.Frame(result_canvas, bg="white", bd=2, relief="groove")
######        frame.pack(pady=10, padx=10, fill="x")
######
######
######        tk.Label(frame, text=f"Medicine: {med_name}", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
######
######        for label, value in details.items():
######            tk.Label(frame, text=f"{label}: {value}", wraplength=600, justify="left", bg="white").pack(anchor='w')
######            tk.Button(frame, text="🔊 Listen", command=lambda t=f"{label}: {value}": speak_text(t)).pack(anchor='w')
######
######    if not found_any:
######        messagebox.showerror("Error", "No known medicine names found in the image.")
######    print("Extracted text:", extracted)
######
######
####### Setup GUI
######root = tk.Tk()
######root.title("MedGuide - AI Medicine Assistant")
######root.geometry("800x800")
######root.configure(bg="white")
######
####### Heading
######tk.Label(root, text="MedGuide - An AI Tool to Assist with Medicines", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)
######tk.Label(root, text="⚠️ It is recommended to consult doctors. Do not rely solely on MedGuide.", fg="red", bg="white").pack(pady=5)
######
####### Buttons
######button_frame = tk.Frame(root, bg="white")
######button_frame.pack(pady=20)
######tk.Button(button_frame, text="📷 Take Photo", font=("Arial", 12), command=upload_photo, bg="#cceeff").pack(side="left", padx=10)
######tk.Button(button_frame, text="📁 Upload Photo", font=("Arial", 12), command=upload_photo, bg="#ccffcc").pack(side="left", padx=10)
######
####### Scrollable result frame
######canvas_container = tk.Frame(root)
######canvas_container.pack(fill="both", expand=True, pady=10)
######
######canvas = tk.Canvas(canvas_container, bg="white")
######scrollbar = tk.Scrollbar(canvas_container, orient="vertical", command=canvas.yview)
######result_canvas = tk.Frame(canvas, bg="white")
######
######result_canvas.bind(
######    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
######)
######
######canvas.create_window((0, 0), window=result_canvas, anchor="nw")
######canvas.configure(yscrollcommand=scrollbar.set)
######
######canvas.pack(side="left", fill="both", expand=True)
######scrollbar.pack(side="right", fill="y")
######
######root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import pandas as pd
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
import tempfile
import pygame

# Initialize pygame
pygame.init()




# Optional: Set path to tesseract executable if not in PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Get medicine details from namesfinal.csv

def get_medicine_details(med_name):
    try:
        df = pd.read_csv(r"C:\Users\Varsh\Desktop\namesfinal.csv", encoding='ISO-8859-1')
        matched = df[df.iloc[:, 0].str.lower().str.contains(med_name.lower())]

        if matched.empty:
            return None

        row = matched.iloc[0]
        details = {}
        for col in df.columns[1:]:
            details[col] = row[col]
        return details

    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

# Speak text using gTTS in selected language
##def speak_text(text, lang='en'):
##    try:
##        tts = gTTS(text=text, lang=lang)
##        with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as fp:
##            tts.save(fp.name)
##            pygame.mixer.music.load(fp.name)
##            pygame.mixer.music.play()
##            while pygame.mixer.music.get_busy():
##                continue
##    except Exception as e:
##        print(f"Audio error: {e}")

def speak_text(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_path = os.path.join(tempfile.gettempdir(), f"medguide_audio_{lang}.mp3")
        tts.save(temp_path)

        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        # Wait until the audio is done playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Now it's safe to delete the file
        pygame.mixer.music.unload()
        os.remove(temp_path)

    except Exception as e:
        print(f"Audio error: {e}")



# Extract text from image
def extract_text(image_path):
    img = Image.open(image_path)
    gray = img.convert('L')
    text = pytesseract.image_to_string(gray)
    return text.strip()

# Handle photo upload
def upload_photo():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    extracted = extract_text(file_path)
    if not extracted.strip():
        messagebox.showerror("Error", "No text found in the image. Please try again with a clearer photo.")
        return

    med_lines = extracted.split('\n')
    found_any = False

    for widget in result_canvas.winfo_children():
        widget.destroy()

    for line in med_lines:
        med_name = line.strip()
        if not med_name:
            continue
        details = get_medicine_details(med_name)
        if not details:
            continue

        found_any = True
        frame = tk.Frame(result_canvas, bg="white", bd=2, relief="groove")
        frame.pack(pady=10, padx=10, fill="x")

        tk.Label(frame, text=f"Medicine: {med_name}", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

        for label, value in details.items():
            en_text = f"{label}: {value}"
            hi_text = GoogleTranslator(source='auto', target='hi').translate(en_text)
            ta_text = GoogleTranslator(source='auto', target='ta').translate(en_text)

            for lang_text, lang_code in zip([en_text, hi_text, ta_text], ['en', 'hi', 'ta']):
                tk.Label(frame, text=lang_text, wraplength=600, justify="left", bg="white").pack(anchor='w')
                tk.Button(frame, text=f"🔊 Listen ({lang_code})", command=lambda t=lang_text, l=lang_code: speak_text(t, l)).pack(anchor='w')

    if not found_any:
        messagebox.showerror("Error", "No known medicine names found in the image.")

# Setup GUI
root = tk.Tk()
root.title("MedGuide - AI Medicine Assistant")
root.geometry("800x800")
root.configure(bg="lavender")

### Heading
##tk.Label(root, text="MedGuide - An AI Tool to Assist with Medicines", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)
##tk.Label(root, text="⚠️ It is recommended to consult doctors. Do not rely solely on MedGuide.", fg="red", bg="white").pack(pady=5)
##

# Heading Frame
heading_frame = tk.Frame(root, bg="#004080", pady=20)
heading_frame.pack(fill="x")

heading_label = tk.Label(
    heading_frame,
    text="💊 MedGuide 💊\nAn AI Tool to Assist with Medicines",
    font=("Comic Sans MS", 28, "bold"),
    bg="#004080",
    fg="white",
    justify="center"
)
heading_label.pack()

# Warning label
tk.Label(
    root,
    text="⚠️ It is recommended to consult doctors. Do not rely solely on MedGuide.",
    font=("Arial", 12, "italic"),
    fg="red",
    bg="#e6f2ff"
).pack(pady=(5, 10))

# Buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)
tk.Button(button_frame, text="📷 Take Photo", font=("Arial", 12), command=upload_photo, bg="#cceeff").pack(side="left", padx=10)
tk.Button(button_frame, text="📁 Upload Photo", font=("Arial", 12), command=upload_photo, bg="#ccffcc").pack(side="left", padx=10)

# Scrollable result frame
canvas_container = tk.Frame(root)
canvas_container.pack(fill="both", expand=True, pady=10)

canvas = tk.Canvas(canvas_container, bg="white")
scrollbar = tk.Scrollbar(canvas_container, orient="vertical", command=canvas.yview)
result_canvas = tk.Frame(canvas, bg="white")

result_canvas.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=result_canvas, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
