# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_boardOfDOzd.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 37))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 0))
        self.frame_9.setStyleSheet(u"background-color: rgb(21, 77, 127);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 2, -1, -1)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 87 10pt \"Nexa Text-Trial Heavy Italic\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(120, 16777215))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.btn_minimize = QPushButton(self.frame_10)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(0, 30))
        self.btn_minimize.setMaximumSize(QSize(30, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"border-radius:15px;")
        self.btn_minimize.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_minimize)

        self.btn_connect_3 = QPushButton(self.frame_10)
        self.btn_connect_3.setObjectName(u"btn_connect_3")
        self.btn_connect_3.setMinimumSize(QSize(0, 30))
        self.btn_connect_3.setMaximumSize(QSize(30, 16777215))
        self.btn_connect_3.setFont(font)
        self.btn_connect_3.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius:15px;")
        self.btn_connect_3.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_connect_3)

        self.btn_close = QPushButton(self.frame_10)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 32))
        self.btn_close.setMaximumSize(QSize(30, 16777215))
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:15px;")
        self.btn_close.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_8)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(21, 77, 127);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_6 = QHBoxLayout(self.home)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.number_plate = QLabel(self.frame_6)
        self.number_plate.setObjectName(u"number_plate")
        self.number_plate.setGeometry(QRect(20, 20, 191, 41))
        self.number_plate.setFont(font)
        self.number_plate.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;\n"
"color:white;")
        self.number_plate.setAlignment(Qt.AlignCenter)
        self.car_color = QLabel(self.frame_6)
        self.car_color.setObjectName(u"car_color")
        self.car_color.setGeometry(QRect(20, 80, 191, 41))
        self.car_color.setFont(font)
        self.car_color.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;\n"
"color:white;")
        self.car_color.setAlignment(Qt.AlignCenter)
        self.car_model = QLabel(self.frame_6)
        self.car_model.setObjectName(u"car_model")
        self.car_model.setGeometry(QRect(20, 140, 191, 41))
        self.car_model.setFont(font)
        self.car_model.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;\n"
"color:white;")
        self.car_model.setAlignment(Qt.AlignCenter)
        self.knust_sequence = QLabel(self.frame_6)
        self.knust_sequence.setObjectName(u"knust_sequence")
        self.knust_sequence.setGeometry(QRect(20, 200, 191, 41))
        self.knust_sequence.setFont(font)
        self.knust_sequence.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;\n"
"color:white;")
        self.knust_sequence.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notification = QLabel(self.frame_7)
        self.notification.setObjectName(u"notification")
        self.notification.setFont(font)
        self.notification.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;")
        self.notification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.notification)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_7.raise_()
        self.frame_6.raise_()

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(21, 77, 127);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cameraFeed = QLabel(self.frame_4)
        self.cameraFeed.setObjectName(u"cameraFeed")
        font1 = QFont()
        font1.setPointSize(12)
        self.cameraFeed.setFont(font1)
        self.cameraFeed.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"")
        self.cameraFeed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cameraFeed)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.btn_connect = QPushButton(self.frame_5)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(100, 30))
        self.btn_connect.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(False)
        self.btn_connect.setFont(font2)
        self.btn_connect.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;")
        self.btn_connect.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_connect)

        self.btn_disconnect = QPushButton(self.frame_5)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(100, 30))
        self.btn_disconnect.setMaximumSize(QSize(16777215, 30))
        self.btn_disconnect.setFont(font)
        self.btn_disconnect.setStyleSheet(u"background-color: rgb(145, 145, 145);\n"
"border-radius:10px;")
        self.btn_disconnect.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_disconnect)

        self.camera_url = QLineEdit(self.frame_5)
        self.camera_url.setObjectName(u"camera_url")
        self.camera_url.setMinimumSize(QSize(0, 30))
        self.camera_url.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(10)
        self.camera_url.setFont(font3)
        self.camera_url.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:2px solid rgb(145, 145, 145);")

        self.horizontalLayout_2.addWidget(self.camera_url)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_3)


        self.horizontalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.home)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KNUST TROSKI AUTHENTICATION SYSTEM", None))
        self.btn_minimize.setText("")
        self.btn_connect_3.setText("")
        self.btn_close.setText("")
        self.number_plate.setText(QCoreApplication.translate("MainWindow", u"Number Plate", None))
        self.car_color.setText(QCoreApplication.translate("MainWindow", u"Car Color", None))
        self.car_model.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.knust_sequence.setText(QCoreApplication.translate("MainWindow", u"KNUST Number", None))
        self.notification.setText(QCoreApplication.translate("MainWindow", u"Notificaton", None))
        self.cameraFeed.setText(QCoreApplication.translate("MainWindow", u"Feed", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
    # retranslateUi

