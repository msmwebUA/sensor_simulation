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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)
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
        self.mainBlockRpmFrame = QFrame(self.mainFrame)
        self.mainBlockRpmFrame.setObjectName(u"mainBlockRpmFrame")
        self.mainBlockRpmFrame.setGeometry(QRect(0, 44, 174, 90))
        self.mainBlockRpmFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainBlockRpmFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainBlockRpmFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.mainBlockRpmFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.configLabel = QLabel(self.mainBlockRpmFrame)
        self.configLabel.setObjectName(u"configLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.configLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.configLabel, 0, 0, 1, 1)

        self.configComboBox = QComboBox(self.mainBlockRpmFrame)
        self.configComboBox.setObjectName(u"configComboBox")

        self.gridLayout_3.addWidget(self.configComboBox, 0, 1, 1, 1)

        self.mainBlockRpmLabel = QLabel(self.mainBlockRpmFrame)
        self.mainBlockRpmLabel.setObjectName(u"mainBlockRpmLabel")
        self.mainBlockRpmLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.mainBlockRpmLabel, 1, 0, 1, 1)

        self.mainBlockRpm = QSpinBox(self.mainBlockRpmFrame)
        self.mainBlockRpm.setObjectName(u"mainBlockRpm")
        self.mainBlockRpm.setMinimumSize(QSize(0, 30))
        self.mainBlockRpm.setMaximumSize(QSize(70, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        self.mainBlockRpm.setFont(font2)
        self.mainBlockRpm.setFrame(True)
        self.mainBlockRpm.setMaximum(5000)

        self.gridLayout_3.addWidget(self.mainBlockRpm, 1, 1, 1, 1)

        self.coefficientsFrame = QFrame(self.mainFrame)
        self.coefficientsFrame.setObjectName(u"coefficientsFrame")
        self.coefficientsFrame.setGeometry(QRect(240, 5, 240, 138))
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
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.coefficientLabel1.setFont(font3)

        self.gridLayout.addWidget(self.coefficientLabel1, 0, 0, 1, 1)

        self.sensor1Coefficient = QLineEdit(self.coefficientsChannelsFrame)
        self.sensor1Coefficient.setObjectName(u"sensor1Coefficient")
        self.sensor1Coefficient.setMinimumSize(QSize(0, 25))
        self.sensor1Coefficient.setMaximumSize(QSize(60, 16777215))
        self.sensor1Coefficient.setFont(font2)

        self.gridLayout.addWidget(self.sensor1Coefficient, 0, 1, 1, 1)

        self.coefficientLabel3 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel3.setObjectName(u"coefficientLabel3")
        self.coefficientLabel3.setFont(font3)

        self.gridLayout.addWidget(self.coefficientLabel3, 0, 2, 1, 1)

        self.sensor3Coefficient = QLineEdit(self.coefficientsChannelsFrame)
        self.sensor3Coefficient.setObjectName(u"sensor3Coefficient")
        self.sensor3Coefficient.setMinimumSize(QSize(0, 25))
        self.sensor3Coefficient.setMaximumSize(QSize(60, 16777215))
        self.sensor3Coefficient.setFont(font2)

        self.gridLayout.addWidget(self.sensor3Coefficient, 0, 3, 1, 1)

        self.coefficientLabel2 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel2.setObjectName(u"coefficientLabel2")
        self.coefficientLabel2.setFont(font3)

        self.gridLayout.addWidget(self.coefficientLabel2, 1, 0, 1, 1)

        self.sensor2Coefficient = QLineEdit(self.coefficientsChannelsFrame)
        self.sensor2Coefficient.setObjectName(u"sensor2Coefficient")
        self.sensor2Coefficient.setMinimumSize(QSize(0, 25))
        self.sensor2Coefficient.setMaximumSize(QSize(60, 16777215))
        self.sensor2Coefficient.setFont(font2)

        self.gridLayout.addWidget(self.sensor2Coefficient, 1, 1, 1, 1)

        self.coefficientLabel4 = QLabel(self.coefficientsChannelsFrame)
        self.coefficientLabel4.setObjectName(u"coefficientLabel4")
        self.coefficientLabel4.setFont(font3)

        self.gridLayout.addWidget(self.coefficientLabel4, 1, 2, 1, 1)

        self.sensor4Coefficient = QLineEdit(self.coefficientsChannelsFrame)
        self.sensor4Coefficient.setObjectName(u"sensor4Coefficient")
        self.sensor4Coefficient.setMinimumSize(QSize(0, 25))
        self.sensor4Coefficient.setMaximumSize(QSize(60, 16777215))
        self.sensor4Coefficient.setFont(font2)

        self.gridLayout.addWidget(self.sensor4Coefficient, 1, 3, 1, 1)

        self.rpmPerSensorFrame = QFrame(self.mainFrame)
        self.rpmPerSensorFrame.setObjectName(u"rpmPerSensorFrame")
        self.rpmPerSensorFrame.setGeometry(QRect(488, 5, 240, 138))
        self.rpmPerSensorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rpmPerSensorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.rpmPerSensorLabel = QLabel(self.rpmPerSensorFrame)
        self.rpmPerSensorLabel.setObjectName(u"rpmPerSensorLabel")
        self.rpmPerSensorLabel.setGeometry(QRect(13, 13, 83, 17))
        self.rpmPerSensorLabel.setFont(font1)
        self.sensorRpmFrame = QFrame(self.rpmPerSensorFrame)
        self.sensorRpmFrame.setObjectName(u"sensorRpmFrame")
        self.sensorRpmFrame.setGeometry(QRect(10, 36, 231, 86))
        self.sensorRpmFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sensorRpmFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.sensorRpmFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sensorRpmLabel1 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel1.setObjectName(u"sensorRpmLabel1")
        self.sensorRpmLabel1.setFont(font3)

        self.gridLayout_2.addWidget(self.sensorRpmLabel1, 0, 0, 1, 1)

        self.sensorRpmLabel3 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel3.setObjectName(u"sensorRpmLabel3")
        self.sensorRpmLabel3.setFont(font3)

        self.gridLayout_2.addWidget(self.sensorRpmLabel3, 0, 2, 1, 1)

        self.sensorRpmLabel2 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel2.setObjectName(u"sensorRpmLabel2")
        self.sensorRpmLabel2.setFont(font3)

        self.gridLayout_2.addWidget(self.sensorRpmLabel2, 1, 0, 1, 1)

        self.sensorRpmLabel4 = QLabel(self.sensorRpmFrame)
        self.sensorRpmLabel4.setObjectName(u"sensorRpmLabel4")
        self.sensorRpmLabel4.setFont(font3)

        self.gridLayout_2.addWidget(self.sensorRpmLabel4, 1, 2, 1, 1)

        self.sensor1Rpm = QSpinBox(self.sensorRpmFrame)
        self.sensor1Rpm.setObjectName(u"sensor1Rpm")
        self.sensor1Rpm.setMinimumSize(QSize(0, 30))
        self.sensor1Rpm.setMaximumSize(QSize(70, 16777215))
        self.sensor1Rpm.setFont(font2)
        self.sensor1Rpm.setFrame(True)
        self.sensor1Rpm.setMaximum(5000)

        self.gridLayout_2.addWidget(self.sensor1Rpm, 0, 1, 1, 1)

        self.sensor2Rpm = QSpinBox(self.sensorRpmFrame)
        self.sensor2Rpm.setObjectName(u"sensor2Rpm")
        self.sensor2Rpm.setMinimumSize(QSize(0, 30))
        self.sensor2Rpm.setMaximumSize(QSize(70, 16777215))
        self.sensor2Rpm.setFont(font2)
        self.sensor2Rpm.setFrame(True)
        self.sensor2Rpm.setMaximum(5000)

        self.gridLayout_2.addWidget(self.sensor2Rpm, 1, 1, 1, 1)

        self.sensor3Rpm = QSpinBox(self.sensorRpmFrame)
        self.sensor3Rpm.setObjectName(u"sensor3Rpm")
        self.sensor3Rpm.setMinimumSize(QSize(0, 30))
        self.sensor3Rpm.setMaximumSize(QSize(70, 16777215))
        self.sensor3Rpm.setFont(font2)
        self.sensor3Rpm.setFrame(True)
        self.sensor3Rpm.setMaximum(5000)

        self.gridLayout_2.addWidget(self.sensor3Rpm, 0, 3, 1, 1)

        self.sensor4Rpm = QSpinBox(self.sensorRpmFrame)
        self.sensor4Rpm.setObjectName(u"sensor4Rpm")
        self.sensor4Rpm.setMinimumSize(QSize(0, 30))
        self.sensor4Rpm.setMaximumSize(QSize(70, 16777215))
        self.sensor4Rpm.setFont(font2)
        self.sensor4Rpm.setFrame(True)
        self.sensor4Rpm.setMaximum(5000)

        self.gridLayout_2.addWidget(self.sensor4Rpm, 1, 3, 1, 1)

        self.manualRpmCheckBox = QCheckBox(self.rpmPerSensorFrame)
        self.manualRpmCheckBox.setObjectName(u"manualRpmCheckBox")
        self.manualRpmCheckBox.setGeometry(QRect(140, 20, 85, 20))
        self.mainBlockLabel = QLabel(self.mainFrame)
        self.mainBlockLabel.setObjectName(u"mainBlockLabel")
        self.mainBlockLabel.setGeometry(QRect(10, 20, 150, 17))
        self.mainBlockLabel.setFont(font1)

        self.verticalLayout_5.addWidget(self.mainFrame)

        self.commandButtonsFrame = QFrame(self.wrapperFrame)
        self.commandButtonsFrame.setObjectName(u"commandButtonsFrame")
        self.commandButtonsFrame.setMinimumSize(QSize(0, 50))
        self.commandButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.commandButtonsFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.commandButtonsFrame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.commandButtonsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navFrameSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.navFrameSpacer1)

        self.simulationBtn = QPushButton(self.commandButtonsFrame)
        self.simulationBtn.setObjectName(u"simulationBtn")
        sizePolicy.setHeightForWidth(self.simulationBtn.sizePolicy().hasHeightForWidth())
        self.simulationBtn.setSizePolicy(sizePolicy)
        self.simulationBtn.setMinimumSize(QSize(150, 40))
        self.simulationBtn.setMaximumSize(QSize(90, 50))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.simulationBtn.setFont(font4)
        self.simulationBtn.setStyleSheet(u"")
        self.simulationBtn.setCheckable(False)
        self.simulationBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.simulationBtn)

        self.navFrameSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.navFrameSpacer2)

        self.controlS1Btn = QPushButton(self.commandButtonsFrame)
        self.controlS1Btn.setObjectName(u"controlS1Btn")
        sizePolicy.setHeightForWidth(self.controlS1Btn.sizePolicy().hasHeightForWidth())
        self.controlS1Btn.setSizePolicy(sizePolicy)
        self.controlS1Btn.setMinimumSize(QSize(92, 40))
        self.controlS1Btn.setMaximumSize(QSize(92, 50))
        self.controlS1Btn.setFont(font4)
        self.controlS1Btn.setStyleSheet(u"")
        self.controlS1Btn.setCheckable(False)
        self.controlS1Btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.controlS1Btn)

        self.controlS2Btn = QPushButton(self.commandButtonsFrame)
        self.controlS2Btn.setObjectName(u"controlS2Btn")
        sizePolicy.setHeightForWidth(self.controlS2Btn.sizePolicy().hasHeightForWidth())
        self.controlS2Btn.setSizePolicy(sizePolicy)
        self.controlS2Btn.setMinimumSize(QSize(92, 40))
        self.controlS2Btn.setMaximumSize(QSize(92, 50))
        self.controlS2Btn.setFont(font4)
        self.controlS2Btn.setStyleSheet(u"")
        self.controlS2Btn.setCheckable(False)
        self.controlS2Btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.controlS2Btn)

        self.controlS3Btn = QPushButton(self.commandButtonsFrame)
        self.controlS3Btn.setObjectName(u"controlS3Btn")
        sizePolicy.setHeightForWidth(self.controlS3Btn.sizePolicy().hasHeightForWidth())
        self.controlS3Btn.setSizePolicy(sizePolicy)
        self.controlS3Btn.setMinimumSize(QSize(92, 40))
        self.controlS3Btn.setMaximumSize(QSize(92, 50))
        self.controlS3Btn.setFont(font4)
        self.controlS3Btn.setStyleSheet(u"")
        self.controlS3Btn.setCheckable(False)
        self.controlS3Btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.controlS3Btn)

        self.controlS4Btn = QPushButton(self.commandButtonsFrame)
        self.controlS4Btn.setObjectName(u"controlS4Btn")
        sizePolicy.setHeightForWidth(self.controlS4Btn.sizePolicy().hasHeightForWidth())
        self.controlS4Btn.setSizePolicy(sizePolicy)
        self.controlS4Btn.setMinimumSize(QSize(92, 40))
        self.controlS4Btn.setMaximumSize(QSize(92, 50))
        self.controlS4Btn.setFont(font4)
        self.controlS4Btn.setStyleSheet(u"")
        self.controlS4Btn.setCheckable(False)
        self.controlS4Btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.controlS4Btn)


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
        font5 = QFont()
        font5.setFamilies([u"Courier New"])
        font5.setPointSize(10)
        self.consoleText.setFont(font5)
        self.consoleText.setStyleSheet(u"background-color: #1e1e1e; color: #ffffff;")

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
        self.configLabel.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.mainBlockRpmLabel.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
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
        self.mainBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Main Block", None))
        self.simulationBtn.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f Start simulation", None))
        self.controlS1Btn.setText(QCoreApplication.translate("MainWindow", u"\u23f9\ufe0f Stop S1", None))
        self.controlS2Btn.setText(QCoreApplication.translate("MainWindow", u"\u23f9\ufe0f Stop S2", None))
        self.controlS3Btn.setText(QCoreApplication.translate("MainWindow", u"\u23f9\ufe0f Stop S3", None))
        self.controlS4Btn.setText(QCoreApplication.translate("MainWindow", u"\u23f9\ufe0f Stop S4", None))
    # retranslateUi

