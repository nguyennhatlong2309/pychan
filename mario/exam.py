from PIL import Image
import os

# Mở ảnh động
img = Image.open("images/Piranha Plant - Blue.gif")

# Tạo thư mục lưu frame
os.makedirs("frames", exist_ok=True)

# Duyệt qua từng frame và lưu ra file riêng
frame = 0
while True:
    img.seek(frame)
    img.save(f"images/Piranha Plant{frame}.png")
    frame += 1
    try:
        img.seek(frame)
    except EOFError:
        break

print("Tách xong!")
