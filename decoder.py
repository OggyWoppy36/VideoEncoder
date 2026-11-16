from pathlib import Path

import cv2
import tkinter as tk
from tkinter import filedialog


# root = tk.Tk()
# root.withdraw()

def decode_file():
    video_path = filedialog.askopenfilename(
        title="Select encoded video to decode",
        filetypes=(("AVI files", "*.avi"),("All files", "*.*"))
    )

    p = Path(video_path)
    if not video_path:
        print("No video selected")
        return
    elif p.suffix != ".avi":
        print(f"Incorrect file type selected ({p.suffix}). Please select a '.avi' file")
        return


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
    name = (p.name)[len("Encoded-video-"):-4]
    suffix = name[:4]
    out_path = filedialog.asksaveasfilename(
        title="Save decoded file as:",
        initialfile=f"Decoded-{name}",
        defaultextension=suffix
    )

    with open(out_path, "wb") as f:
        f.write(byte_arr)
    print(f"File decoded and saved to {out_path}")