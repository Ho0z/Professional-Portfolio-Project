from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk, ImageEnhance

# ----------------- Functions -----------------
def select_base_image():
    global base_img, base_display
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path:
        base_img = Image.open(path).convert("RGBA")
        display_image(base_img)

def select_watermark():
    global watermark_img
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path:
        watermark_img = Image.open(path).convert("RGBA")
        # Optional: resize watermark if too big
        w, h = base_img.size
        watermark_img.thumbnail((w//4, h//4))
        add_watermark()

def add_watermark():
    global watermarked_img
    if base_img and watermark_img:
        watermarked_img = base_img.copy()
        # Set transparency
        alpha = watermark_img.split()[3]
        alpha = alpha.point(lambda p: p * 0.5)  # 50% transparency
        watermark_img.putalpha(alpha)
        
        # Position: bottom right
        bx, by = base_img.size
        wx, wy = watermark_img.size
        position = (bx - wx - 10, by - wy - 10)
        
        watermarked_img.paste(watermark_img, position, watermark_img)
        display_image(watermarked_img)

def display_image(img):
    tk_img = ImageTk.PhotoImage(img.resize((400, 300)))
    image_label.config(image=tk_img)
    image_label.image = tk_img

def save_image():
    if watermarked_img:
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if path:
            watermarked_img.save(path)

# ----------------- GUI Setup -----------------
base_img = None
watermark_img = None
watermarked_img = None

root = Tk()
root.title("Watermarking App")
root.minsize(500, 400)

image_label = Label(root)
image_label.pack(pady=10)

btn_base = Button(root, text="Select Base Image", command=select_base_image)
btn_base.pack(pady=5)

btn_watermark = Button(root, text="Select Watermark", command=select_watermark)
btn_watermark.pack(pady=5)

btn_save = Button(root, text="Save Watermarked Image", command=save_image)
btn_save.pack(pady=5)

root.mainloop()