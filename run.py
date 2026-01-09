import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
import time

ASCII_CHARS = "@%#*+=-:. "
WIDTH_CHARS = 120
EDGE_BLEND = 0.35
CONTRAST = 1.1
FPS_LIMIT = 20

def preprocess(image):
    image = image.convert("L")
    image = ImageOps.autocontrast(image, cutoff=2)
    image = ImageEnhance.Contrast(image).enhance(CONTRAST)

    if EDGE_BLEND > 0:
        edges = image.filter(ImageFilter.FIND_EDGES)
        image = Image.blend(image, edges, EDGE_BLEND)

    image = ImageOps.autocontrast(image, cutoff=1)
    return image

def pixel_to_char(px):
    return ASCII_CHARS[int(px / 255 * (len(ASCII_CHARS) - 1))]

def frame_to_ascii(frame):
    image = Image.fromarray(frame)
    w, h = image.size
    aspect = h / w
    height_chars = int(WIDTH_CHARS * aspect * 0.55)

    image = image.resize((WIDTH_CHARS, height_chars))
    image = preprocess(image)

    pixels = np.array(image)
    return [
        "".join(pixel_to_char(px) for px in row)
        for row in pixels
    ]

def ascii_to_image(lines):
    font = ImageFont.load_default()

    # Pillow-safe character size
    bbox = font.getbbox("A")
    char_w = bbox[2] - bbox[0]
    char_h = bbox[3] - bbox[1]

    img_w = char_w * len(lines[0])
    img_h = char_h * len(lines)

    img = Image.new("L", (img_w, img_h), 255)
    draw = ImageDraw.Draw(img)

    for y, line in enumerate(lines):
        draw.text((0, y * char_h), line, fill=0, font=font)

    return np.array(img)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not available")
        return

    last_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        now = time.time()
        if now - last_time < 1 / FPS_LIMIT:
            continue
        last_time = now

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        ascii_lines = frame_to_ascii(frame)
        ascii_img = ascii_to_image(ascii_lines)

        cv2.imshow("ASCII Camera", ascii_img)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
