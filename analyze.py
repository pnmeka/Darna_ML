import pytesseract
from pdf2image import convert_from_path
import os
import variables

# Importing variables from variables.py
HS_path = variables.HS_path
ocr_files = variables.ocr_files
upload_dir = variables.upload_dir
folderpath = variables.Health_files
ip_address = variables.ip_address

# Path to the Tesseract OCR executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Directory path for OCR files
ocr_files_dir = f'{ocr_files}/'

# Create the ocr_files/pytess directory if it doesn't exist
output_dir = os.path.join(ocr_files_dir, 'pytess')
os.makedirs(output_dir, exist_ok=True)

# Function to perform OCR on an image file
def perform_ocr(image_path):
    try:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image_path)
        return text
    except pytesseract.TesseractError as e:
        print(f"Error processing image: {image_path}")
        print(f"Error message: {str(e)}")
        return None

# Function to convert a PDF file to images
def convert_pdf_to_images(file_path):
    try:
        # Convert PDF to images using pdf2image library
        images = convert_from_path(file_path)
        return images
    except Exception as e:
        print(f"Error converting PDF to images: {file_path}")
        print(f"Error message: {str(e)}")
        return None

# Function to iterate through files in the directory and perform OCR
def process_ocr_files(directory):
    # Create the ocr_results.txt file in the pytess directory
    output_file = os.path.join(output_dir, 'ocr_results.txt')
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    # Check if the file is a PDF
                    if file_name.lower().endswith('.pdf'):
                        # Convert PDF to images
                        images = convert_pdf_to_images(file_path)
                        if images is not None:
                            for i, image in enumerate(images):
                                # Perform OCR on each image
                                text = perform_ocr(image)
                                if text is not None:
                                    # Write the extracted text to the output file
                                    f.write(f"File: {file_name}, Page: {i+1}\n")
                                    f.write(text)
                                    f.write('\n\n')

                    else:
                        # Perform OCR on non-PDF files
                        text = perform_ocr(file_path)
                        if text is not None:
                            # Write the extracted text to the output file
                            f.write(f"File: {file_name}\n")
                            f.write(text)
                            f.write('\n\n')

    print('OCR completed. Results saved in', output_file)

# Perform OCR on the files in the directory
process_ocr_files(ocr_files_dir)

