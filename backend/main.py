import os
import sqlite3
import sys
import winsound
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2

import pytesseract
import numpy as np
import imutils

from dashboard.ui_home import Ui_MainWindow
from launcher.ui_Launcher import Ui_Launcher

GLOBAL_STATE =0
counter = 0

font = cv2.FONT_HERSHEY_SIMPLEX
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe' # path location of installed pytesseract

class Main(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_main = Ui_MainWindow()
        self.timer = QTimer()
        self.ui_main.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()

        self.ui_main.btn_close.clicked.connect(self.close)
        self.ui_main.btn_minimize.clicked.connect(self.showMaximized)
        self.ui_main.btn_minimize.clicked.connect(self.showMinimized)
        
        self.ui_main.btn_connect.clicked.connect(self.start_webcam)
        self.ui_main.btn_disconnect.clicked.connect(self.stop_webcam)
        self.create_database_table()
    
        
    def string_formater(self, value: str): 
        return "\'{}\'".format(value) 

    def fetch_car_details(self, plate_id: str):  # function to fetch car details
        details = self.query_car_records(f'SELECT * FROM tb_cars WHERE number_plate={self.string_formater(plate_id)}')
        if len(details) > 0:
            self.render_car_details_to_ui(details)
            winsound.Beep(1000,1000)
        else:
            self.show_info(f"Oops! no details found for\nplate Id: {plate_id}")

    def render_car_details_to_ui(self, details: list): # function to render car details to UI
        self.ui_main.number_plate.setText(str(details[1]))
        self.ui_main.car_model.setText(str(details[2]))
        self.ui_main.car_color.setText(str(details[3]))
        self.ui_main.knust_sequence.setText(str(details[4]))
        
    def query_car_records(self, query): # function to connect and querying car database
        db = sqlite3.connect(self.resource_path('troski_system.db'))
        cursor = db.cursor()
        cursor.execute(query)
        details = cursor.fetchone()
        db.commit()
        cursor.close()
        db_data = []
        if details:
            for data in details:
                db_data.append(data)
        return db_data
    
    def resource_path(self, relative_path):   #loading files from current working directory
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))
        return path
    
    def create_database_table(self): #function to create tables for the existiing database 
        sql= """
            CREATE TABLE IF NOT EXISTS tb_cars(
                generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
                number_plate varchar(15) NOT NULL UNIQUE,
                car_model varchar(20)  NOT NULL,
                car_color varchar(20)  NOT NULL,
                car_number INTEGER  NOT NULL UNIQUE
                )
            """
        db = sqlite3.connect(self.resource_path('troski_system.db'))
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
          
    def start_webcam(self): # function to start/activate web camera
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture = cv2.VideoCapture(0)
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 280)
        self.system_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 450)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)
        self.show_info("Starting webcam in\nprogress.")

    def update_frame(self): # function to handle camera feed activities
        location = None
        ret, self.frame = self.system_capture.read()
        self.gray = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)
        self.bfilter = cv2.bilateralFilter(self.gray, 11, 17, 17) #Noise reduction
        self.edged = cv2.Canny(self.bfilter , 30, 200) #Edge detection
        keypoints = cv2.findContours(self.edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break
        mask = np.zeros(self.gray.shape, np.uint8)
        cv2.drawContours(mask, [location], 0 ,255, -1)
        cv2.bitwise_and(self.frame, self.frame, mask=mask)
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = self.gray[x1:x2+1, y1:y2+1]
        sharpen_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])  # sharpening of the image
        gray2= cv2.cvtColor(cropped_image, cv2.COLOR_BAYER_BG2GRAY)
        #sharp_image = cv2.filter2D(gray2,-1,sharpen_filter)
        text = pytesseract.image_to_string(cropped_image, lang="eng", config='--psm 3')
        self.fetch_car_details(text)
        cv2.putText(self.frame, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
        cv2.rectangle(self.frame, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),1)
        self.display_feed(self.frame, 1)


    def display_feed(self, image, window=1): # renders camera feed to the label
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui_main.cameraFeed.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui_main.cameraFeed.setScaledContents(True)

    def show_info(self, content: str): # shows status of the extracted character based on database info
        self.ui_main.notification.setText(content)

    def stop_webcam(self): # function to stop/disconnect web camera
        if self.timer.isActive():
            self.show_info("Disconnected from\nwebcam.")
            self.ui_main.cameraFeed.setPixmap("")
            # self.ui_main.cameraFeed.setScaledContents(False)
            self.timer.stop()
        else:
            self.show_info("Oops! no camera\nin use.")
    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event): # function to help move the window around
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

class Launcher(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_Launcher()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.splashscreen.setGraphicsEffect(self.shadow)
    
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()


    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.close()  
            self.main = Main()
            self.main.show()        
        counter +=1


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Launcher()  
    sys.exit(application.exec_())