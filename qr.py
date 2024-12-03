import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import webbrowser

def generate_qr_code():
    print("Choose the type of QR Code to generate:")
    print("1. Website URL")
    print("2. Contact Details (vCard)")
    print("3. Payment Link (PhonePe/UPI)")
    print("4. Wi-Fi Configuration")
    print("5. Custom Text")
    print("6. Decode a QR Code")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        # Website URL
        website = input("Enter the website URL: ")
        data = website

    elif choice == "2":
        # Contact Details (vCard)
        name = input("Enter full name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        company = input("Enter company name: ")
        data = f"""
        VCARD
        FN:{name}
        TEL:{phone}
        EMAIL:{email}
        ORG:{company}
        """

    elif choice == "3":
        # Payment Link (PhonePe or Bank Account)
        upi_id = input("Enter the UPI ID (e.g., 9666030787@bank): ")
        amount = input("Enter the amount to be credited (optional, press Enter to skip): ")

        # UPI payment format
        data = f"upi://pay?pa={upi_id}&pn=Payment"
        if amount:
            data += f"&am={amount}"

    elif choice == "4":
        # Wi-Fi Configuration
        wifi_ssid = input("Enter Wi-Fi SSID: ")
        wifi_password = input("Enter Wi-Fi password: ")
        wifi_auth = input("Enter Authentication Type (WPA/WEP/None): ")

        # Wi-Fi QR code format
        data = f"WIFI:S:{wifi_ssid};T:{wifi_auth};P:{wifi_password};;"

    elif choice == "5":
        # Custom Text
        custom_text = input("Enter the custom text: ")
        data = custom_text

    elif choice == "6":
        # Decode a QR Code
        decode_qr_code()
        return

    else:
        print("Invalid choice! Exiting.")
        return

    # Create QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR Code image
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the QR Code
    filename = input("Enter the filename to save the QR Code (e.g., 'QRCode.png'): ")
    img.save(filename)

    print(f"QR Code generated and saved as '{filename}'")

def decode_qr_code():
    print("Decoding QR Code...")
    # Get the file path of the QR code image
    file_path = input("Enter the file path of the QR Code image to decode: ")

    # Use pyzbar to decode the QR Code
    try:
        img = Image.open(file_path)
        decoded_data = decode(img)

        if decoded_data:
            for obj in decoded_data:
                decoded_text = obj.data.decode('utf-8')
                print(f"Decoded Data: {decoded_text}")
                # If the decoded data is a URL, ask if the user wants to open it
                if decoded_text.startswith("http://") or decoded_text.startswith("https://") or decoded_text.startswith('www.')or decoded_text.endswith('.com'):
                    open_website = input("Would you like to open this website? (yes/no): ").strip().lower()
                    if open_website == 'yes':
                        webbrowser.open(decoded_text)
                        print(f"Opening {decoded_text} in browser.")
                    else:
                        print("Website not opened.")
                break  # Exit after the first successful decode (since QR code typically has one data field)
        else:
            print("No QR Code found or unable to decode the image.")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
generate_qr_code()
