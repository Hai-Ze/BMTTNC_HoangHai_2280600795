import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message) - 15):  # Giảm 16 bit kết thúc
        char = binary_message[i:i+8]
        if binary_message[i:i+16] == '1111111111111110':  # Kiểm tra 16 bit kết thúc
            break
        if len(char) == 8:  # Đảm bảo chỉ lấy byte đầy đủ
            message += chr(int(char, 2))

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()