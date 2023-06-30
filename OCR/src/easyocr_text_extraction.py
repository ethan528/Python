import sys
import easyocr
from PIL import Image

def load_image(file_path):
    return Image.open(file_path)

def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    return result

def write_extracted_text_to_file(text_result, file_path):
    with open(file_path, "w") as output_file:
        for item in text_result:
            output_file.write(item[1])
            output_file.write("\n")

if __name__ == "__main__":
    input_image_path = sys.argv[1]
   
# python easyocr_text_extraction.py input_image_path output_text_path