# Hiding-a-text-inside-the-image-using-stenography
🕵️‍♀️ Image Steganography: Hide & Extract Text in Images
A simple yet effective tool to securely hide and retrieve secret messages in .png images using the Least Significant Bit (LSB) technique.

✨ Features
🔐 Text Hiding – Embed hidden messages in PNG images.

🔍 Text Extraction – Accurately retrieve hidden text from stego-images.

🧠 Simple Logic – Uses the classic LSB method for steganography.

⚡ Lightweight & Fast – No heavy dependencies or GPU needed.

🚀 Getting Started
🔧 Prerequisites
Make sure you have Python installed (Python 3.6+).

Install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
🛠 Usage
🖊️ To Hide a Message in an Image
bash
Copy
Edit
python hide_text.py
Input: Source image (.png)

Output: New image with hidden text

🕵️‍♂️ To Extract the Hidden Message
bash
Copy
Edit
python extract_text.py
Input: Stego-image (.png)

Output: Revealed secret message in the terminal

📁 File Structure
bash
Copy
Edit
├── hide_text.py          # Script to hide secret message in an image
├── extract_text.py       # Script to extract hidden message
├── utils.py              # Common utility functions
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation
