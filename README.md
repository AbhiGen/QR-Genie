
# QR Genie

**QR Genie** is a Python-based QR code generator and decoder. It allows users to create QR codes for URLs, contact information, payment links, Wi-Fi configurations, custom text, and more. Additionally, QRify decodes QR codes, making it easy to retrieve and interact with the encoded data.

## Features
- Create QR codes for various purposes: Website URLs, vCard contact info, UPI payment links, Wi-Fi configuration, and custom text.
- Decode QR codes and access the encoded data.
- Option to open websites directly from decoded URLs.

---

## Getting Started

Follow these steps to set up and run **QRify** on your local machine.

### Prerequisites

- Python 3.x installed on your machine.
- A terminal or command prompt for running commands.

### 1. Setting Up a Virtual Environment

To ensure dependencies are isolated and your system remains clean, create a virtual environment.

#### On Windows:
```bash
python -m venv qrify_env
```

#### On macOS/Linux:
```bash
python3 -m venv qrify_env
```

### 2. Activating the Virtual Environment

#### On Windows:
```bash
qrify_env\Scripts\activate
```

#### On macOS/Linux:
```bash
source qrify_env/bin/activate
```

After activation, you should see the environment name in your terminal (e.g., `(qrify_env)`).

### 3. Installing Required Packages

Once the virtual environment is activated, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one with the necessary packages:

```bash
pip install qrcode[pil] pyzbar Pillow opencv-python
```

This installs:
- `qrcode` for generating QR codes.
- `pyzbar` for decoding QR codes.
- `Pillow` for image handling.
- `opencv-python` (optional) for image processing.

### 4. Running the Project

To run the QRify project, use the following command:

```bash
python qrify.py
```

Follow the on-screen prompts to generate or decode QR codes.

### 5. Deactivating the Virtual Environment

Once you're done, deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your system’s default Python environment.

---

## Example Use Case

1. **Generate a Website QR Code:**
   - Select option `1` for Website URL.
   - Enter a valid URL (e.g., `https://www.example.com`).
   - The QR code will be generated and saved as an image.

2. **Decode a QR Code:**
   - Select option `6` to decode a QR code.
   - Provide the file path to the QR code image.
   - If the QR code contains a website URL, you will be prompted to open it in your browser.

---

## Troubleshooting

- **Module Not Found Error**: Ensure that all dependencies are installed in your virtual environment.
- **File Not Found Error for QR Code Image**: Double-check the file path you entered when decoding the QR code.

---

## Acknowledgements

- **qrcode**: Python library for generating QR codes.
- **pyzbar**: Python library for reading QR codes.
- **Pillow**: Python Imaging Library (PIL) for image processing.
- **OpenCV**: Optional library for image processing and reading QR codes.

---

You can customize this template as per the project specifics, including file paths or other dependencies you might need.
