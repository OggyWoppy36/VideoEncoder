from pathlib import Path

import cv2
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select encoded video to decode",
    filetypes=(("AVI files", "*.avi"), ("All files", "*.*"))
)



cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_ct = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

byte_arr = bytearray()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    byte_arr.extend(frame.tobytes())

cap.release()
p = Path(video_path)
name = (p.name).split("-")[-1][:-4]
print(name)
out_path = filedialog.asksaveasfilename(
    title="Save decoded file as:",
    initialfile=f"Decoded-{name}",
    defaultextension=name[:-4]
)

with open(out_path, "wb") as f:
    f.write(byte_arr)
print(f"File decoded and saved to {out_path}")