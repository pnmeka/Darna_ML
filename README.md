# Darna_ML; ### WORK IN PROGRESS ####
This module works along with Darna_local at : https://github.com/seapoe1809/Darna_local


This module will take input from user and then scans your data using OCR, deidentifies it based on your input and finallys generate useful health intent/ information. Please note this is a build on Darna.HI local and builds on the cognition of the Darna.HI which allows self custody of your data. There are several parts to the module
 

a) analyze.py is a Tesseract based OCR engine, deidentifier and an  USPTF based recommendation algorithm that analyzes files in Darna_local that are auto filtered to ocr_files depending on their extension. It creates a text dump and tries to tag information accumulated into a file called ocr_results.txt 
b) It then runs a deidentification engine that removes identifying data. This could help is interacting with AI LLM models to get answers or also to generate useful prompts for the AI LLM model.
c) Finally using USPTF based algorithm it lists out Grade A recommendations which are usually followed by your Primary Physician for your age and sex and enters them in a text document. Please note this is just health intent document and isnt designed to provide medical advice. You should consult your doctor for it
d) All files are stored in the Darna_tesseract subdirectory of ocr_files

**Steps:**
Step 1

              $cd Health_server

Step 2

              $git clone https://github.com/pnmeka/Darna_ML/

Step 3

              cd Darna_ML

Step 4       Replace user with your username so that the path matches

              $cp analyze.py /home/< user >/Health_server/
              
Step 5        Replace user with your username so that the path matches

              $cp analyze.html /home/< user >/Health_server/templates

Step 6
              copy code from darna_flask and paste it in lieu of section @app.route('/analyze) into darna.py

            
Step 7       Return back to Health_server directory

              $cd ..

Step 8      Relaunch darna.py

              $python3 darna.py

              




References:
1. https://www.uspreventiveservicestaskforce.org/
2. chat GPT
