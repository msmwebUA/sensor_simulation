# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 466)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.wrapperFrame = QFrame(self.mainPage)
        self.wrapperFrame.setObjectName(u"wrapperFrame")
        self.wrapperFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.wrapperFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.wrapperFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.headerFrame = QFrame(self.wrapperFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(30, 60))
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.logo = QLabel(self.headerFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(20, 40))
        self.logo.setMaximumSize(QSize(55, 40))
        self.logo.setPixmap(QPixmap(u":/img/img/3k-logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.heading = QLabel(self.headerFrame)
        self.heading.setObjectName(u"heading")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.heading.setFont(font)

        self.horizontalLayout.addWidget(self.heading)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.settingsBtn = QPushButton(self.headerFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy)
        self.settingsBtn.setMinimumSize(QSize(90, 40))
        self.settingsBtn.setMaximumSize(QSize(90, 40))
        self.settingsBtn.setStyleSheet(u"")
        self.settingsBtn.setCheckable(False)
        self.settingsBtn.setFlat(False)

        self.horizontalLayout.addWidget(self.settingsBtn)


        self.verticalLayout_5.addWidget(self.headerFrame)

        self.mainFrame = QFrame(self.wrapperFrame)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setMinimumSize(QSize(0, 150))
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.mainFrame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.mainBlockRpmFrame = QFrame(self.mainFrame)
        self.mainBlockRpmFrame.setObjectName(u"mainBlockRpmFrame")
        self.mainBlockRpmFrame.setMaximumSize(QSize(120, 16777215))
        self.mainBlockRpmFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainBlockRpmFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainBlockRpmFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainBlockRpmLabel = QLabel(self.mainBlockRpmFrame)
        self.mainBlockRpmLabel.setObjectName(u"mainBlockRpmLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.mainBlockRpmLabel.setFont(font1)

        self.verticalLayout_3.addWidget(self.mainBlockRpmLabel)

        self.rpmLabel = QLabel(self.mainBlockRpmFrame)
        self.rpmLabel.setObjectName(u"rpmLabel")
        font2 = QFont()
        font2.setBold(True)
        self.rpmLabel.setFont(font2)

        self.verticalLayout_3.addWidget(self.rpmLabel)

        self.mainBlockRpm = QSpinBox(self.mainBlockRpmFrame)
        self.mainBlockRpm.setObjectName(u"mainBlockRpm")
        self.mainBlockRpm.setMinimumSize(QSize(0, 30))
        self.mainBlockRpm.setMaximumSize(QSize(70, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        self.mainBlockRpm.setFont(font3)
        self.mainBlockRpm.setFrame(True)
        self.mainBlockRpm.setMaximum(5000)

        self.verticalLayout_3.addWidget(self.mainBlockRpm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.mainBlockRpmFrame)

        self.coefficientsFrame = QFrame(self.mainFrame)
        self.coefficientsFrame.setObjectName(u"coefficientsFrame")
        self.coefficientsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.coefficientsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.coefficientsLabel = QLabel(self.coefficientsFrame)
        self.coefficientsLabel.setObjectName(u"coefficientsLabel")
        self.coefficientsLabel.setGeometry(QRect(13, 13, 151, 17))
        self.coefficientsLabel.setFont(font1)
        self.coefficientsChannelsFrame = QFrame(self.coefficientsFrame)
        self.coefficientsChannelsFrame.setObjectName(u"coefficientsChannelsFrame")
        self.coefficientsChannelsFrame.setGeometry(QRect(10, 40, 231, 86))
        self.coefficientsChannelsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.coefficientsChannelsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.coefficientsChannelsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.coefficientLabel1 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel1.setObjectName(u"coefficientLabel1")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.coefficientLabel1.setFont(font4)

        self.gridLayout.addWidget(self.coefficientLabel1, 0, 0, 1, 1)

        self.coefficient1 = QLineEdit(self.coefficientsChannelsFrame)
        self.coefficient1.setObjectName(u"coefficient1")
        self.coefficient1.setMinimumSize(QSize(0, 25))
        self.coefficient1.setMaximumSize(QSize(60, 16777215))
        self.coefficient1.setFont(font3)

        self.gridLayout.addWidget(self.coefficient1, 0, 1, 1, 1)

        self.coefficientLabel3 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel3.setObjectName(u"coefficientLabel3")
        self.coefficientLabel3.setFont(font4)

        self.gridLayout.addWidget(self.coefficientLabel3, 0, 2, 1, 1)

        self.coefficient3 = QLineEdit(self.coefficientsChannelsFrame)
        self.coefficient3.setObjectName(u"coefficient3")
        self.coefficient3.setMinimumSize(QSize(0, 25))
        self.coefficient3.setMaximumSize(QSize(60, 16777215))
        self.coefficient3.setFont(font3)

        self.gridLayout.addWidget(self.coefficient3, 0, 3, 1, 1)

        self.coefficientLabel2 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel2.setObjectName(u"coefficientLabel2")
        self.coefficientLabel2.setFont(font4)

        self.gridLayout.addWidget(self.coefficientLabel2, 1, 0, 1, 1)

        self.coefficient2 = QLineEdit(self.coefficientsChannelsFrame)
        self.coefficient2.setObjectName(u"coefficient2")
        self.coefficient2.setMinimumSize(QSize(0, 25))
        self.coefficient2.setMaximumSize(QSize(60, 16777215))
        self.coefficient2.setFont(font3)

        self.gridLayout.addWidget(self.coefficient2, 1, 1, 1, 1)

        self.coefficientLabel4 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel4.setObjectName(u"coefficientLabel4")
        self.coefficientLabel4.setFont(font4)

        self.gridLayout.addWidget(self.coefficientLabel4, 1, 2, 1, 1)

        self.coefficient4 = QLineEdit(self.coefficientsChannelsFrame)
        self.coefficient4.setObjectName(u"coefficient4")
        self.coefficient4.setMinimumSize(QSize(0, 25))
        self.coefficient4.setMaximumSize(QSize(60, 16777215))
        self.coefficient4.setFont(font3)

        self.gridLayout.addWidget(self.coefficient4, 1, 3, 1, 1)


        self.horizontalLayout_3.addWidget(self.coefficientsFrame)

        self.rpmPerSensorFrame = QFrame(self.mainFrame)
        self.rpmPerSensorFrame.setObjectName(u"rpmPerSensorFrame")
        self.rpmPerSensorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rpmPerSensorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.rpmPerSensorLabel = QLabel(self.rpmPerSensorFrame)
        self.rpmPerSensorLabel.setObjectName(u"rpmPerSensorLabel")
        self.rpmPerSensorLabel.setGeometry(QRect(13, 13, 83, 17))
        self.rpmPerSensorLabel.setFont(font1)
        self.sensorRpmFrame = QFrame(self.rpmPerSensorFrame)
        self.sensorRpmFrame.setObjectName(u"sensorRpmFrame")
        self.sensorRpmFrame.setGeometry(QRect(13, 46, 207, 86))
        self.sensorRpmFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sensorRpmFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.sensorRpmFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sensorRpmLabel1 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel1.setObjectName(u"sensorRpmLabel1")
        self.sensorRpmLabel1.setFont(font4)

        self.gridLayout_2.addWidget(self.sensorRpmLabel1, 0, 0, 1, 1)

        self.sensor1Rpm = QLineEdit(self.sensorRpmFrame)
        self.sensor1Rpm.setObjectName(u"sensor1Rpm")
        self.sensor1Rpm.setMinimumSize(QSize(0, 25))
        self.sensor1Rpm.setMaximumSize(QSize(60, 16777215))
        self.sensor1Rpm.setFont(font3)

        self.gridLayout_2.addWidget(self.sensor1Rpm, 0, 1, 1, 1)

        self.sensorRpmLabel3 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel3.setObjectName(u"sensorRpmLabel3")
        self.sensorRpmLabel3.setFont(font4)

        self.gridLayout_2.addWidget(self.sensorRpmLabel3, 0, 2, 1, 1)

        self.sensor3Rpm = QLineEdit(self.sensorRpmFrame)
        self.sensor3Rpm.setObjectName(u"sensor3Rpm")
        self.sensor3Rpm.setMinimumSize(QSize(0, 25))
        self.sensor3Rpm.setMaximumSize(QSize(60, 16777215))
        self.sensor3Rpm.setFont(font3)

        self.gridLayout_2.addWidget(self.sensor3Rpm, 0, 3, 1, 1)

        self.sensorRpmLabel2 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel2.setObjectName(u"sensorRpmLabel2")
        self.sensorRpmLabel2.setFont(font4)

        self.gridLayout_2.addWidget(self.sensorRpmLabel2, 1, 0, 1, 1)

        self.sensor2Rpm = QLineEdit(self.sensorRpmFrame)
        self.sensor2Rpm.setObjectName(u"sensor2Rpm")
        self.sensor2Rpm.setMinimumSize(QSize(0, 25))
        self.sensor2Rpm.setMaximumSize(QSize(60, 16777215))
        self.sensor2Rpm.setFont(font3)

        self.gridLayout_2.addWidget(self.sensor2Rpm, 1, 1, 1, 1)

        self.sensorRpmLabel4 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel4.setObjectName(u"sensorRpmLabel4")
        self.sensorRpmLabel4.setFont(font4)

        self.gridLayout_2.addWidget(self.sensorRpmLabel4, 1, 2, 1, 1)

        self.sensor4Rpm = QLineEdit(self.sensorRpmFrame)
        self.sensor4Rpm.setObjectName(u"sensor4Rpm")
        self.sensor4Rpm.setMinimumSize(QSize(0, 25))
        self.sensor4Rpm.setMaximumSize(QSize(60, 16777215))
        self.sensor4Rpm.setFont(font3)

        self.gridLayout_2.addWidget(self.sensor4Rpm, 1, 3, 1, 1)

        self.manualRpmCheckBox = QCheckBox(self.rpmPerSensorFrame)
        self.manualRpmCheckBox.setObjectName(u"manualRpmCheckBox")
        self.manualRpmCheckBox.setGeometry(QRect(190, 20, 85, 20))

        self.horizontalLayout_3.addWidget(self.rpmPerSensorFrame)


        self.verticalLayout_5.addWidget(self.mainFrame)

        self.commandButtonsFrame = QFrame(self.wrapperFrame)
        self.commandButtonsFrame.setObjectName(u"commandButtonsFrame")
        self.commandButtonsFrame.setMinimumSize(QSize(0, 50))
        self.commandButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.commandButtonsFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.commandButtonsFrame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.commandButtonsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.navFrameSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.navFrameSpacer1)

        self.simulationBtn = QPushButton(self.commandButtonsFrame)
        self.simulationBtn.setObjectName(u"simulationBtn")
        sizePolicy.setHeightForWidth(self.simulationBtn.sizePolicy().hasHeightForWidth())
        self.simulationBtn.setSizePolicy(sizePolicy)
        self.simulationBtn.setMinimumSize(QSize(150, 40))
        self.simulationBtn.setMaximumSize(QSize(90, 50))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.simulationBtn.setFont(font5)
        self.simulationBtn.setStyleSheet(u"")
        self.simulationBtn.setCheckable(False)
        self.simulationBtn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.simulationBtn)

        self.navFrameSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.navFrameSpacer2)


        self.verticalLayout_5.addWidget(self.commandButtonsFrame)

        self.consoleFrame = QFrame(self.wrapperFrame)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setMinimumSize(QSize(0, 100))
        self.consoleFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.consoleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.consoleFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.consoleText = QPlainTextEdit(self.consoleFrame)
        self.consoleText.setObjectName(u"consoleText")
        self.consoleText.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.consoleText)


        self.verticalLayout_5.addWidget(self.consoleFrame)


        self.verticalLayout_2.addWidget(self.wrapperFrame)

        self.stackedWidget.addWidget(self.mainPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sensor Simulation", None))
        self.logo.setText("")
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Sensor Simulation", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f Settings", None))
        self.mainBlockRpmLabel.setText(QCoreApplication.translate("MainWindow", u"Main Block", None))
        self.rpmLabel.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.coefficientsLabel.setText(QCoreApplication.translate("MainWindow", u"Coefficients (x/y)", None))
        self.coefficientLabel1.setText(QCoreApplication.translate("MainWindow", u"Ch 1", None))
        self.coefficientLabel3.setText(QCoreApplication.translate("MainWindow", u"Ch 3", None))
        self.coefficientLabel2.setText(QCoreApplication.translate("MainWindow", u"Ch 2", None))
        self.coefficientLabel4.setText(QCoreApplication.translate("MainWindow", u"Ch 4", None))
        self.rpmPerSensorLabel.setText(QCoreApplication.translate("MainWindow", u"RPM/Sensor", None))
        self.sensorRpmLabel1.setText(QCoreApplication.translate("MainWindow", u"S1", None))
        self.sensorRpmLabel3.setText(QCoreApplication.translate("MainWindow", u"S3", None))
        self.sensorRpmLabel2.setText(QCoreApplication.translate("MainWindow", u"S2", None))
        self.sensorRpmLabel4.setText(QCoreApplication.translate("MainWindow", u"S4", None))
        self.manualRpmCheckBox.setText(QCoreApplication.translate("MainWindow", u"Manually", None))
        self.simulationBtn.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f Start simulation", None))
    # retranslateUi

