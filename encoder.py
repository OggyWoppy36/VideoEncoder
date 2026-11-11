import cv2
from itertools import batched
import numpy as np
from pathlib import Path
from tkinter import filedialog



# Video Resolution
WIDTH = 640
HEIGHT = 480
BYTES_PER_FRAME = WIDTH*HEIGHT*3
FPS = 5

file_path = filedialog.askopenfilename(
    title="Select a file to encode",
    filetypes=(("Text files", "*.txt"),("All files", "*.*"))
)

p = Path(file_path)
video_file_name = f"Encoded-video-{p.name}.avi"

if file_path:
    with open(file_path, "rb") as file:
        data = file.read()
        print(f"Successfully loaded {file_path}")
else:
    print("No file was selected.")
    data = b""

byte_arr = np.frombuffer(data, dtype=np.uint8) # gets in 8 bit values
byte_ct = len(byte_arr)
extra = byte_ct % BYTES_PER_FRAME
if extra > 0:
    last_frame_padding = BYTES_PER_FRAME - extra
    byte_arr = np.pad(byte_arr, (0, last_frame_padding), mode='constant', constant_values=0)

frame_bytes = batched(byte_arr, BYTES_PER_FRAME)

frames = []
for frame in frame_bytes:
    frame_grid = np.fromiter(frame, dtype=np.uint8).reshape((HEIGHT, WIDTH, 3)) # height x width x 3 RGB
    frames.append(frame_grid)


fourcc = cv2.VideoWriter_fourcc(*"FFV1")
output = cv2.VideoWriter(video_file_name, fourcc, FPS, frameSize=(WIDTH, HEIGHT), isColor=True)

for frame in frames:
    output.write(frame)

output.release()
print("Video compiled!")