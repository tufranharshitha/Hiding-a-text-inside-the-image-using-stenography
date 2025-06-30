import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from utils import bin_to_text

def extract_text(image_path):
    img = Image.open(image_path)
    binary_data = ""
    for pixel in img.getdata():
        for color in pixel[:3]:  # R, G, B
            binary_data += str(color & 1)

    eof = binary_data.find('1111111111111110')
    if eof != -1:
        binary_data = binary_data[:eof]
    return bin_to_text(binary_data)

def choose_file():
    path = filedialog.askopenfilename(filetypes=[("PNG images", "*.png")])
    if path:
        image_path_var.set(path)

def start_extract():
    img_path = image_path_var.get()
    if not img_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    message = extract_text(img_path)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, message)

# GUI Setup
root = tk.Tk()
root.title("Steganography - Extract Hidden Text")

tk.Label(root, text="Select Image with Hidden Text:").pack()
image_path_var = tk.StringVar()
tk.Entry(root, textvariable=image_path_var, width=50).pack()
tk.Button(root, text="Browse", command=choose_file).pack(pady=5)

tk.Button(root, text="Extract Text", command=start_extract).pack(pady=10)

tk.Label(root, text="Extracted Message:").pack()
text_box = tk.Text(root, height=6, width=50)
text_box.pack()

root.mainloop()
