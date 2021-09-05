import sys
from os import walk
import os
import cv2
from PIL import Image
import pytesseract
import torch
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Result(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Results")
        self.setFixedSize(1010, 640)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(100, 90, 821, 491))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        item.setText("License Plate Number")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setText("Violations")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setText("Contact")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        item.setText("Send Notification")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(400, 20, 221, 41))
        self.label.setText("RESULTS")
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

class Processing(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Please Wait")
        self.setFixedSize(762, 528)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(70, 90, 621, 341))
        self.textEdit.setReadOnly(True)
        
        self.label = QLabel(self)
        self.label.setText("Processing....")
        self.label.setGeometry(QRect(70, 40, 291, 31))
        font = QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        
        
        self.pushButton = QPushButton(self)
        self.pushButton.setText("View Results")
        self.pushButton.setGeometry(QRect(330, 460, 141, 41))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.hide()

class Admin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Helmet Detection with YOLO v5")
        self.setFixedSize(550,300)

        
        self.label = QLabel(self)
        self.label.setGeometry(QRect(150, 20, 241, 41))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("ADMINISTRATOR")
        self.label.setObjectName("label")
        
        
        self.inp = QLineEdit(self)
        self.inp.setGeometry(QRect(50, 120, 351, 31))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.inp.setFont(font)
        self.inp.setText("")
        self.inp.setReadOnly(True)
        
        
        self.browse = QPushButton(self)
        self.browse.setGeometry(QRect(440, 120, 51, 31))
        self.browse.setText("...")
        
        
        self.done = QPushButton(self)
        self.done.setGeometry(QRect(220, 220, 101, 41))
        self.done.setText("Done")
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.done.setFont(font)
        self.done.hide()

class Driver():
    def __init__(self):
        self.admin = Admin()
        self.admin.browse.clicked.connect(self.browse_folder)
        self.admin.show()

    def initial(self):
        with open(os.path.expanduser('inil.txt'),'r') as f:
            self.read = f.readlines()
            for i in range(len(self.read)):
                self.read[i] = self.read[i][:-1]


    def browse_folder(self):
        self.src = QFileDialog.getExistingDirectory(None,'Select a Folder:','C:\\',QFileDialog.ShowDirsOnly)
        self.admin.inp.setText(self.src)
        self.admin.done.show()
        self.admin.done.clicked.connect(self.redirect)

    def redirect(self):
        self.processing = Processing()
        self.processing.show()
        self.processing.textEdit.append("Extracting data from : "+self.src)
        helmet_src = next(walk(self.src), (None, None, []))[2]
        self.processing.textEdit.append(str(len(helmet_src))+" files found")
        
        for i in range(len(helmet_src)):
            img = cv2.imread(str(self.src+"/"+helmet_src[i]))
            cv2.imwrite("./src/"+str(i+1)+".jpg",img)
        
        self.processing.textEdit.append("Extraction complete!")
        self.processing.textEdit.append(str(len(helmet_src))+" files stored locally in folder \'src\'")
        self.processing.textEdit.append("Detecting Helmet Violations")
        self.execute()
        self.processing.pushButton.show()
        self.processing.pushButton.clicked.connect(self.results)
    
    def execute(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

        helmet_src = next(walk('./src/'), (None, None, []))[2] 

        self.processing.textEdit.append("Yolo v5 model loaded and ready!")
        self.processing.textEdit.append(str(len(helmet_src))+" files are being processed in the model")

        for i in range(len(helmet_src)):
            helmet_src[i] = "./src/"+helmet_src[i]

        model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/helmet_detection_best.pt', source='local', force_reload=True)

        model.conf = 0.4 
        model.classes = [0]

        result = model(helmet_src)
        result.crop(save_dir='./detect/helmet/')

        helmet_dest = next(walk('./detect/helmet/crops/0/'), (None, None, []))[2]  

        self.processing.textEdit.append(str(len(helmet_dest))+" vehicles detected")

        for i in range(len(helmet_dest)):
            helmet_dest[i] = "./detect/helmet/crops/0/"+helmet_dest[i]


        model.classes = [1,2]
        model.conf = 0.25
        helmet_result = model(helmet_dest,640)
        helmet_result.save(save_dir='./detect/helmet/dest/')

        ref = next(walk('./detect/helmet/dest/'), (None, None, []))[2]
        license_src = []
        for i in range(len(helmet_result.pandas().xyxy)):
            for j in helmet_result.pandas().xyxy[i].values.tolist():
                if j[5] == 2:
                    license_src.append(ref[i])
        for i in range(len(license_src)):
            license_src[i] = "./detect/helmet/dest/"+license_src[i]
        
        self.processing.textEdit.append("Violations Confirmed")
        
        license_model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/license_plate_best.pt', source='local', force_reload=True)

        result = license_model(license_src)
        result.crop(save_dir='./yolov5/detect/license/')

        license_src = next(walk('./yolov5/detect/license/crops/numberplate'), (None, None, []))[2] 

        for i in range(len(license_src)):
            license_src[i] = "./yolov5/detect/license/crops/numberplate/"+license_src[i]

        self.initial()
        
        for i in license_src:
            self.read.append(pytesseract.image_to_string(Image.open(i)))

        self.processing.textEdit.append("Loading Results")

    def results(self):
        self.result = Result()
        ref = list(set(self.read))

        self.result.tableWidget.setRowCount(100)
        self.result.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i in range(1,len(ref)):
            self.result.tableWidget.setItem(i-1,0,QTableWidgetItem(ref[i]))
            self.result.tableWidget.setItem(i-1,1,QTableWidgetItem(str(self.read.count(ref[i]))))
            self.result.tableWidget.setItem(i-1,2,QTableWidgetItem('9182545882'))
            self.result.tableWidget.setItem(i-1,3,QTableWidgetItem('Click to notify'))
        self.result.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = Driver()
    sys.exit(app.exec_())
