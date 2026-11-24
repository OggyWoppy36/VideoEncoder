import tkinter as tk
from encoder import encode_file
from decoder import decode_file
import os.path as path
import sys

def res_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)


root = tk.Tk()
root.title("Video Encoder & Decoder")

wwidth = 320
wheight = 180
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
x = (swidth // 2) - (wwidth // 2)
y = (sheight // 3) - (wheight // 2)

root.geometry(f"{wwidth}x{wheight}+{x}+{y}")
bgcol = "#000515"
root.configure(bg=bgcol)

txtcol = "#64ABF0"
imgcol = "#38D1FB"

columns_frame = tk.Frame(root, bg=bgcol)
columns_frame.pack(fill="x", padx=30, expand=True)

encode_frame = tk.Frame(columns_frame, bg=bgcol)
encode_frame.pack(side="left")

encode_img = tk.PhotoImage(file=res_path("icon-encode.png"))
button_encode = tk.Button(
    encode_frame,
    image=encode_img,
    bg=imgcol,
    fg="#FFFFFF",
    padx=15,
    pady=0,
    command=encode_file,
    width=100,
    height=100
)
button_encode.pack(pady=0)

encode_label =  tk.Label(
    encode_frame,
    text="Encode file...",
    bg=bgcol,
    fg=txtcol
)
encode_label.pack(pady=10)


decode_frame = tk.Frame(columns_frame, bg=bgcol)
decode_frame.pack(side="right")

decode_img = tk.PhotoImage(file=res_path("icon-decode.png"))
button_decode = tk.Button(
    decode_frame,
    image=decode_img,
    bg=imgcol,
    fg="#FFFFFF",
    padx=15,
    pady=0,
    command=decode_file,
    width=100,
    height=100
)
button_decode.pack(pady=0)

decode_label =  tk.Label(
    decode_frame,
    text="Decode file...",
    bg=bgcol,
    fg=txtcol
)
decode_label.pack(pady=10)

root.mainloop()
