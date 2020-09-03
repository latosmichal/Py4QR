import sys
from QRdetector import DetectQRAndWriteToFile

if __name__ == "__main__":
    argumentList = sys.argv[1:]
    for imagePath in argumentList:
        DetectQRAndWriteToFile(imagePath)
