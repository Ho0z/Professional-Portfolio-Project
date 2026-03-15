from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk, ImageEnhance

def select_base_image():
    global base_img
    base_img = Image.open("/Users/hozaifaabdrabou/Desktop/Paython/Professional Portfolio Project/4. Watermarking Desktop App/image.png").convert("RGBA")

def select_watermark_image():
    global watermark_img, position
    watermark_img = Image.open("/Users/hozaifaabdrabou/Desktop/Paython/Professional Portfolio Project/4. Watermarking Desktop App/image2.png").convert("RGBA")
    
    # Optional: resize watermark if too big
    w, h = base_img.size
    watermark_img.thumbnail((w//4, h//4))

    # Add watermark (50% transparency)
    alpha = watermark_img.split()[3]
    alpha = alpha.point(lambda p: p * 0.5)
    watermark_img.putalpha(alpha)

    # Position: bottom-right corner
    bx, by = base_img.size
    wx, wy = watermark_img.size
    position = (bx - wx - 10, by - wy - 10)
    add_watermark()

def add_watermark():
    base_img.paste(watermark_img,position, watermark_img)
    watermarked_img = base_img
    watermarked_img.show()

#-------------~
window = Tk()
window.title("Watermarking App")
window.minsize(500, 400)

image_label = Label(window)
image_label.pack(pady=10)

btn_base = Button(window, text="Select Base Image", command=select_base_image)
btn_base.pack(pady=5)

btn_watermark = Button(window, text="Select Watermark", command=select_watermark_image)
btn_watermark.pack(pady=5)

btn_save = Button(window, text="Save Watermarked Image", command='')
btn_save.pack(pady=5)

window.mainloop()