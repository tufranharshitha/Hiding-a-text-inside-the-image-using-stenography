
def text_to_bin(text):
    return ''.join([format(ord(i), '08b') for i in text])

def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(b, 2)) for b in chars])
