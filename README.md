# Darna_ML; ### WORK IN PROGRESS ####
This module works along with Darna_local at : https://github.com/seapoe1809/Darna_local


This module will take input from user and generate useful health intent/ information. Please note this is a build on Darna.HI local and builds on the cognition of the Darna.HI which allows self custody of your data. There are several parts to the module

a)  gen_rec.py is a USPTF based recommendation algorithm. Once you input your age and gender, it should list out Grade A recommendations which are usually followed by your Primary Physician. The data is sourced from : https://www.uspreventiveservicestaskforce.org/apps/

b) analyze.html is a Tesseract based OCR engine that analyzes files in Darna_local that are auto filtered to ocr_files depending on their extension. It creates a text dump and tries to tag information accumulated into a file called ocr_results.txt





References:
1. https://www.uspreventiveservicestaskforce.org/
2. chat GPT
