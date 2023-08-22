# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LauncherCQldWV.ui'
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
        MainWindow.resize(468, 270)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splashscreen = QFrame(self.centralwidget)
        self.splashscreen.setObjectName(u"splashscreen")
        self.splashscreen.setStyleSheet(u"background-color: rgb(21, 77, 127);")
        self.splashscreen.setFrameShape(QFrame.StyledPanel)
        self.splashscreen.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.splashscreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(6, 90, 411, 41))
        self.label.setStyleSheet(u"\n"
"\n"
"font: 81 13pt \"Montserrat ExtraBold\";\n"
"\n"
"color: rgb(204, 204, 204);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.splashscreen)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 236, 451, 20))
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.splashscreen)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KNUST TROSKI AUTHENTICATION SYSTEM ", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

