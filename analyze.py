import pytesseract
from pdf2image import convert_from_path
import os
import variables
#deidentify records
import re
from datetime import datetime

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
output_dir = os.path.join(ocr_files_dir, 'Darna_tesseract')
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
                if os.path.isfile(file_path) and not file_name.startswith('.'):  # Ignore hidden files
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
print("ocr_results.txt saved in the ocr_files/Darna_tesseract directory")
print("Now deidentifying the data pending your input")



# Load medical record text 
with open(f'{ocr_files}/Darna_tesseract/ocr_results.txt') as f:
  text = f.read()

# Define the patterns to identify and deidentify
#remove anything after keyword
KEYWORDS_REGEX = r'(?i)(?:Name|DOB|Date of birth|Birth|Address|Phone|PATIENT|Patient|MRN|Medical Record Number|APT|House|Street|ST|zip|pin):.*?(\n|$)'
#remove specific words
IGNORE_REGEX = r'(?i)(?<!\bNO\b[-.,])(?:NO\b[-.]|[Nn][Oo]\b[-.,]|fir|last|234|causeway)'
KEYWORDS_REPLACE = r'\1REDACT'
#NAME_REGEX = r'\b(?!(?:NO\b|NO\b[-.]|[Nn][Oo]\b[-.,]))(?:[A-Z][a-z]+\s){1,2}(?:[A-Z][a-z]+)(?<!\b[A-Z]{2}\b)\b'

DOB_REGEX = r'\b(?!(?:NO\b|NO\b[-.]|[Nn][Oo]\b[-.,]))(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2]\d|3[0-1])-\d{4}\b'
SSN_REGEX = r'\b(?!(?:NO\b|NO\b[-.]|[Nn][Oo]\b[-.,]))(\d{3})-(\d{4})\b'
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
ZIP_REGEX = r'\b(?!(?:NO\b|NO\b[-.]|[Nn][Oo]\b[-.,]))([A-Z]{2}) (\d{5})\b'


# Function to generate fake replacement text for keywords
def generate_fake_text(match):
    return re.sub(KEYWORDS_REGEX, KEYWORDS_REPLACE, match.group())

def redact_zip_and_words(match):
    words = match.group(1)
    zip_code = match.group(2)
    redacted_words = 'ZZ ' * min(4, len(words.split()))

    # Redact numbers in groups of 5 digits
    redacted_zip = re.sub(r'\b\d{5}\b', '11111', zip_code)

    return redacted_words + redacted_zip


redacted = re.sub(KEYWORDS_REGEX, generate_fake_text, text, flags=re.IGNORECASE)
redacted = re.sub(IGNORE_REGEX, '', redacted)
#redacted = re.sub(NAME_REGEX, '', redacted)
redacted = re.sub(DOB_REGEX, '', redacted)
redacted = re.sub(SSN_REGEX, '', redacted)
redacted = re.sub(EMAIL_REGEX, '', redacted)
redacted = re.sub(ZIP_REGEX, redact_zip_and_words, redacted)

# Add Deidentification and Date tags
def add_deidentification_tags(text):
    return f'Deidentified Entry | {datetime.now().strftime("%m/%d/%Y")}\n{text}'

tagged = add_deidentification_tags(redacted)

# Write output to new file
with open(f'{ocr_files}/Darna_tesseract/deidentified_records.txt', 'w') as f:
  f.write(tagged)
