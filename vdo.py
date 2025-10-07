import cv2
import time
import shutil

def frame_to_ascii(frame):
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    terminal_size = shutil.get_terminal_size()
    width = min(terminal_size.columns, 80)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height = int(width * frame.shape[0] / frame.shape[1] * 0.55)
    resized = cv2.resize(gray, (width, height))
    
    ascii_image = ""
    for row in resized:
        for pixel in row:
            ascii_image += ascii_chars[pixel * len(ascii_chars) // 256]
        ascii_image += "\n"
    return ascii_image

cap = cv2.VideoCapture("ssstik.io_@sadiya.borsha6_1759799803022.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
frame_delay = 1 / fps if fps > 0 else 0.033

while True:
    start_time = time.time()  # ⏱️ ফ্রেম প্রসেস শুরু
    
    ret, frame = cap.read()
    if not ret:
        break
    
    ascii_art = frame_to_ascii(frame)
    
    # ANSI escape দিয়ে fast clear
    print("\033[H\033[J", end="")
    print(ascii_art)
    
    # ফ্রেম প্রসেসিং টাইম অনুযায়ী adjust sleep
    elapsed = time.time() - start_time
    time_to_sleep = max(0, frame_delay - elapsed)
    time.sleep(time_to_sleep)

cap.release()
