import argparse
import pytesseract
import cv2
import os
import ntpath
from PIL import Image

# Path to the location of the Tesseract-OCR executable/command
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            return word
        else:
            return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--path', type=str, required=True,
                    help="Path to input files")
    args = vars(ap.parse_args())
    base_dir = args["path"]
    s = args["path"]
    dir_path = s.replace(os.sep, ntpath.sep)
    res = os.listdir(dir_path)
    
    filePath = os.path.join(base_dir, r"extractText.txt")

    file = open(filePath, "a")

    for i in res:
        filename = i
        imagePath = os.path.join(base_dir, filename)
        extract = pytesseract.image_to_string(Image.open(imagePath))
        file.write(extract.lower())
        file.write("\n")

    file.close()
    
    phi = []
    with open (r'PHI.txt', 'rt') as myfile: 
        for myline in myfile:
            phi = myline.split(',')
    
    resultPath = os.path.join(base_dir, r"result.txt")

    resultfile = open(resultPath, "a")

    for info in phi:
        resWord = search_str(filePath, info)
        if resWord != 0:
            resultfile.write(resWord)
            resultfile.write("\n")
    
    resultfile.close()