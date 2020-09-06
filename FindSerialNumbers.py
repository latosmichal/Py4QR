import sys
import os
from QRdetector import DetectQRAndWriteToFile
imgPath = "./testImages/"
if __name__ == "__main__":
    argumentList = sys.argv[1:]
    if len(argumentList) > 0:
        for imagePath in argumentList:
            DetectQRAndWriteToFile(imagePath)
    else:
        for file in os.listdir(imgPath):
            if "detectedQR" not in file:
                DetectQRAndWriteToFile(imgPath + file)