
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from utils import text_to_bin

def hide_text(image_path, secret_text, output_path):
    img = Image.open(image_path)
    binary_secret = text_to_bin(secret_text) + '1111111111111110'  # EOF marker
    data_index = 0
    img_data = list(img.getdata())

    for i in range(len(img_data)):
        pixel = list(img_data[i])
        for j in range(3):  # R, G, B
            if data_index < len(binary_secret):
                pixel[j] = pixel[j] & ~1 | int(binary_secret[data_index])
                data_index += 1
        img_data[i] = tuple(pixel)
        if data_index >= len(binary_secret):
            break

    img.putdata(img_data)
    img.save(output_path)
    messagebox.showinfo("Success", f"Text hidden and saved to:\n{output_path}")

def choose_file():
    path = filedialog.askopenfilename(filetypes=[("PNG images", "*.png")])
    if path:
        image_path_var.set(path)

def start_hide():
    img_path = image_path_var.get()
    secret = text_entry.get("1.0", tk.END).strip()
    if not img_path or not secret:
        messagebox.showerror("Error", "Select image and enter a message.")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG images", "*.png")])
    if output_path:
        hide_text(img_path, secret, output_path)

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Hide Text")

tk.Label(root, text="Select Image (PNG):").pack()
image_path_var = tk.StringVar()
tk.Entry(root, textvariable=image_path_var, width=50).pack()
tk.Button(root, text="Browse", command=choose_file).pack(pady=5)

tk.Label(root, text="Enter Secret Message:").pack()
text_entry = tk.Text(root, height=6, width=50)
text_entry.pack()

tk.Button(root, text="Hide Text", command=start_hide).pack(pady=10)

root.mainloop()
