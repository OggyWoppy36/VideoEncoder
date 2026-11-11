import numpy as np
import PIL
import tkinter as tk
from tkinter import filedialog

file_path = filedialog.askopenfilename(
    title="Select a file to encode",
    filetypes=(("Text files", "*.txt"),("All files", "*.*"))
)

if file_path:
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
        print(f"Successfully loaded {file_path}")
else:
    print("No file was selected.")


for byte in data:
    pass