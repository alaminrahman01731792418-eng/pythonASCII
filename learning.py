from PIL import Image, ImageDraw, ImageFont

# ===============================
# ছবির path
image_path = "Snapchat-182861726.jpg"
# ===============================

# ছবি লোড
img = Image.open(image_path)

# PC-friendly width
new_width = 100
width, height = img.size
aspect_ratio = height / width
new_height = int(aspect_ratio * new_width * 0.5)
img = img.resize((new_width, new_height))

# গ্রেস্কেল
img = img.convert('L')

# ASCII ক্যারেক্টার সেট
chars = "@%#*+=-:. "
pixels = img.getdata()
new_pixels = [chars[pixel * len(chars) // 256] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# লাইনে ভাগ
ascii_image = [new_pixels[i:i + new_width] for i in range(0, len(new_pixels), new_width)]
ascii_image_text = "\n".join(ascii_image)

# কনসোলে দেখাও
print(ascii_image_text)

# Text file-এ সংরক্ষণ
with open("ascii_art_pc.txt", "w") as f:
    f.write(ascii_image_text)

print("\nASCII art PC-ready ফাইলে সংরক্ষণ করা হলো: ascii_art_pc.txt")

# ===============================
# ASCII কে PNG তে convert করা
# ===============================
# Font সেট করা (Courier Monospace)
font_size = 10
try:
    font = ImageFont.truetype("cour.ttf", font_size)  # Windows এ Courier
except:
    font = ImageFont.load_default()

# Image সাইজ হিসাব
char_width, char_height = font.getsize("A")
img_width = char_width * new_width
img_height = char_height * len(ascii_image)

# নতুন image তৈরি (সাদা background)
img_ascii = Image.new("L", (img_width, img_height), color=255)
draw = ImageDraw.Draw(img_ascii)

# ASCII text draw করা
y = 0
for line in ascii_image:
    draw.text((0, y), line, fill=0, font=font)  # কালো text
    y += char_height

# PNG হিসেবে save করা
img_ascii.save("ascii_art_pc.png")
print("ASCII art PNG হিসেবে save করা হলো: ascii_art_pc.png")
