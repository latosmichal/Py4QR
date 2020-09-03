import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os


def QRDetect(image, path):
    for barcode in decode(image):
        myData = barcode.data.decode("utf-8")
        # Drawing a rectangle around a QR code
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(image, [points], True, (255, 0, 255), 2)
        # Saving an image with rectangle around QR Code
        detectedQRonImage = path.split(".")[0] + "detectedQR.jpg"
        cv2.imwrite(detectedQRonImage, image)
        return myData.split(";")


def GetDataFromQR(table):
    settingsDict = {}
    print(f"Data = {table}")
    if table:
        for item in table:
            try:
                row = item.split(":", 1)
                settingsDict[row[0]] = row[1]
            except:
                raise Exception("Unrecognized format, probably missing ':' in data set")
        return settingsDict
    else:
        raise Exception("No data detected")


def FindSerial(settingsDict):
    try:
        return settingsDict["SN"]
    except:
        raise Exception("Not found Serial Number in QR Code")


def DetectQRAndWriteToFile(imagePath):
    if os.path.isfile(imagePath):
        img = cv2.imread(imagePath)
        decodedQR = QRDetect(img, imagePath)
        qrData = GetDataFromQR(decodedQR)
        serialNumber = FindSerial(qrData)
        with open("SerialNumber.txt", "a") as File:
            File.write(serialNumber + "\n")
            print(serialNumber)
    else:
        print("Not found a file: " + imagePath)
