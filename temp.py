import qrcode
import os

def generate_qr_code(text, filename="qrcode.png"):
    """
    Generates a QR code from the given text and saves it as an image file.

    Args:
        text (str): The text data to encode in the QR code.
        filename (str): The name of the output image file (e.g., "my_qr_code.png").
    """
    if not text:
        print("Error: Please provide text to generate the QR code.")
        return

    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Ensure the 'qrcodes' directory exists
        output_dir = "qrcodes"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the image
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)
        print(f"QR code generated successfully and saved as '{output_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("--- Text to QR Code Generator ---")
    user_text = input("Enter the text you want to convert to a QR code: ")
    output_filename = input("Enter the desired filename for the QR code image (e.g., my_qr.png, press Enter for default 'qrcode.png'): ")

    if not output_filename:
        generate_qr_code(user_text)
    else:
        # Ensure the filename has a .png extension if not provided
        if not output_filename.lower().endswith(".png"):
            output_filename += ".png"
        generate_qr_code(user_text, output_filename)
