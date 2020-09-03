# Python QR Code detector
This program detects QR Code on picture, decodes its message and draws a rectangle around QR Code.   
![DetectedQR](testImages/1detectedQR.jpg)<img src="testImages/1detectedQR.jpg width=250px height=250px">  
Then it extracts "SN" value from QR data.  
The recognized QR Code is saved as new file within location of the input file.  
Serial Number is saved to text file in root directory "SerialNumber.txt".
## Installation
Navigate to the project's folder and execute:
```
git clone nazwarepo
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
## Running
You can use as many image files as you want.
```
python FindSerialNumbers.py testImages\1.jpg testImages\TEST4.jpg
```