# Video Encoder

Desktop application built with Tkinter and open-cv that translates files between video and their original format.
Includes a simple GUI with file prompts to select the file to encode/decode.

## How it Works
- Encoder: Reads the uploaded file in binary and translates each set of 3 bytes to an R, G, and B value at a certain pixel in the 640x480p grid. It then writes the pixel data to an AVI file using the lossless FFV1 codec.
- Decoder: Reads the frames from the uploaded video using openCV and then flattens the data back into the original bytes

## How to Run (Windows Only)
- Download the exe from the [releases](https://github.com/OggyWoppy36/VideoEncoder/releases) section of this repo.
- Run it, and windows defender will likely flag it, just click "More", then "Run Anyway"

## How to Run (Self-Compiled)
- Requirements:
  - Python 3.15+
- Create a virtual environment
```bash
py -3.15 -m venv venv
.\venv\Scripts\Activate
```
- Install dependencies
```bash
pip install opencv-python numpy pillow pyinstaller
```
- Run the program
```bash
python application.py
```
