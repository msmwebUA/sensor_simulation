# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(800, 240)
        settingsDialog.setModal(True)
        self.actionsButtonsFrame = QFrame(settingsDialog)
        self.actionsButtonsFrame.setObjectName(u"actionsButtonsFrame")
        self.actionsButtonsFrame.setGeometry(QRect(10, 0, 582, 56))
        self.actionsButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.actionsButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.actionsButtonsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.configLabel = QLabel(self.actionsButtonsFrame)
        self.configLabel.setObjectName(u"configLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.configLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.configLabel)

        self.configComboBox = QComboBox(self.actionsButtonsFrame)
        self.configComboBox.setObjectName(u"configComboBox")
        self.configComboBox.setMinimumSize(QSize(0, 37))

        self.horizontalLayout_2.addWidget(self.configComboBox)

        self.manageConfigBtnsFrame = QFrame(self.actionsButtonsFrame)
        self.manageConfigBtnsFrame.setObjectName(u"manageConfigBtnsFrame")
        self.manageConfigBtnsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.manageConfigBtnsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.manageConfigBtnsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.addConfigBtn = QPushButton(self.manageConfigBtnsFrame)
        self.addConfigBtn.setObjectName(u"addConfigBtn")
        self.addConfigBtn.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout.addWidget(self.addConfigBtn)

        self.renameConfigBtn = QPushButton(self.manageConfigBtnsFrame)
        self.renameConfigBtn.setObjectName(u"renameConfigBtn")
        self.renameConfigBtn.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout.addWidget(self.renameConfigBtn)

        self.deleteConfigBtn = QPushButton(self.manageConfigBtnsFrame)
        self.deleteConfigBtn.setObjectName(u"deleteConfigBtn")
        self.deleteConfigBtn.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout.addWidget(self.deleteConfigBtn)


        self.horizontalLayout_2.addWidget(self.manageConfigBtnsFrame)

        self.configNameLabel = QLabel(self.actionsButtonsFrame)
        self.configNameLabel.setObjectName(u"configNameLabel")
        self.configNameLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.configNameLabel)

        self.configName = QLineEdit(self.actionsButtonsFrame)
        self.configName.setObjectName(u"configName")
        self.configName.setMinimumSize(QSize(0, 25))
        self.configName.setMaximumSize(QSize(60, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.configName.setFont(font1)

        self.horizontalLayout_2.addWidget(self.configName)

        self.saveConfigNameBtn = QPushButton(self.actionsButtonsFrame)
        self.saveConfigNameBtn.setObjectName(u"saveConfigNameBtn")

        self.horizontalLayout_2.addWidget(self.saveConfigNameBtn)

        self.mainFrame = QFrame(settingsDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(10, 40, 781, 161))
        self.mainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.defaultValuesFrame = QFrame(self.mainFrame)
        self.defaultValuesFrame.setObjectName(u"defaultValuesFrame")
        self.defaultValuesFrame.setGeometry(QRect(10, 10, 391, 151))
        self.defaultValuesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.defaultValuesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.defaultValuesLabel = QLabel(self.defaultValuesFrame)
        self.defaultValuesLabel.setObjectName(u"defaultValuesLabel")
        self.defaultValuesLabel.setGeometry(QRect(10, 10, 371, 101))
        self.defaultValuesLabel.setFont(font)
        self.replaceWithCurrentValuesBtn = QPushButton(self.defaultValuesFrame)
        self.replaceWithCurrentValuesBtn.setObjectName(u"replaceWithCurrentValuesBtn")
        self.replaceWithCurrentValuesBtn.setGeometry(QRect(200, 120, 181, 32))
        self.sensorGpioFrame = QFrame(self.mainFrame)
        self.sensorGpioFrame.setObjectName(u"sensorGpioFrame")
        self.sensorGpioFrame.setGeometry(QRect(410, 10, 241, 151))
        self.sensorGpioFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sensorGpioFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.sensorGpioLabel = QLabel(self.sensorGpioFrame)
        self.sensorGpioLabel.setObjectName(u"sensorGpioLabel")
        self.sensorGpioLabel.setGeometry(QRect(13, 13, 131, 17))
        self.sensorGpioLabel.setFont(font)
        self.sensorGpioPinsFrame = QFrame(self.sensorGpioFrame)
        self.sensorGpioPinsFrame.setObjectName(u"sensorGpioPinsFrame")
        self.sensorGpioPinsFrame.setGeometry(QRect(10, 36, 191, 94))
        self.sensorGpioPinsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sensorGpioPinsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.sensorGpioPinsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.s1Label = QLabel(self.sensorGpioPinsFrame)
        self.s1Label.setObjectName(u"s1Label")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.s1Label.setFont(font2)

        self.gridLayout.addWidget(self.s1Label, 0, 0, 1, 1)

        self.sensor1Gpio = QSpinBox(self.sensorGpioPinsFrame)
        self.sensor1Gpio.setObjectName(u"sensor1Gpio")
        self.sensor1Gpio.setMinimumSize(QSize(0, 30))
        self.sensor1Gpio.setMaximumSize(QSize(70, 16777215))
        self.sensor1Gpio.setFont(font1)
        self.sensor1Gpio.setFrame(True)
        self.sensor1Gpio.setMaximum(5000)

        self.gridLayout.addWidget(self.sensor1Gpio, 0, 1, 1, 1)

        self.s3Label = QLabel(self.sensorGpioPinsFrame)
        self.s3Label.setObjectName(u"s3Label")
        self.s3Label.setFont(font2)

        self.gridLayout.addWidget(self.s3Label, 0, 2, 1, 1)

        self.sensor3Gpio = QSpinBox(self.sensorGpioPinsFrame)
        self.sensor3Gpio.setObjectName(u"sensor3Gpio")
        self.sensor3Gpio.setMinimumSize(QSize(0, 30))
        self.sensor3Gpio.setMaximumSize(QSize(70, 16777215))
        self.sensor3Gpio.setFont(font1)
        self.sensor3Gpio.setFrame(True)
        self.sensor3Gpio.setMaximum(5000)

        self.gridLayout.addWidget(self.sensor3Gpio, 0, 3, 1, 1)

        self.s2Label = QLabel(self.sensorGpioPinsFrame)
        self.s2Label.setObjectName(u"s2Label")
        self.s2Label.setFont(font2)

        self.gridLayout.addWidget(self.s2Label, 1, 0, 1, 1)

        self.sensor2Gpio = QSpinBox(self.sensorGpioPinsFrame)
        self.sensor2Gpio.setObjectName(u"sensor2Gpio")
        self.sensor2Gpio.setMinimumSize(QSize(0, 30))
        self.sensor2Gpio.setMaximumSize(QSize(70, 16777215))
        self.sensor2Gpio.setFont(font1)
        self.sensor2Gpio.setFrame(True)
        self.sensor2Gpio.setMaximum(5000)

        self.gridLayout.addWidget(self.sensor2Gpio, 1, 1, 1, 1)

        self.s4Label = QLabel(self.sensorGpioPinsFrame)
        self.s4Label.setObjectName(u"s4Label")
        self.s4Label.setFont(font2)

        self.gridLayout.addWidget(self.s4Label, 1, 2, 1, 1)

        self.sensor4Gpio = QSpinBox(self.sensorGpioPinsFrame)
        self.sensor4Gpio.setObjectName(u"sensor4Gpio")
        self.sensor4Gpio.setMinimumSize(QSize(0, 30))
        self.sensor4Gpio.setMaximumSize(QSize(70, 16777215))
        self.sensor4Gpio.setFont(font1)
        self.sensor4Gpio.setFrame(True)
        self.sensor4Gpio.setMaximum(5000)

        self.gridLayout.addWidget(self.sensor4Gpio, 1, 3, 1, 1)

        self.dialogBtnsFrame = QFrame(settingsDialog)
        self.dialogBtnsFrame.setObjectName(u"dialogBtnsFrame")
        self.dialogBtnsFrame.setGeometry(QRect(610, 190, 178, 51))
        self.dialogBtnsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.dialogBtnsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.dialogBtnsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancelBtn = QPushButton(self.dialogBtnsFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_3.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(self.dialogBtnsFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.saveBtn)


        self.retranslateUi(settingsDialog)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"Settings", None))
        self.configLabel.setText(QCoreApplication.translate("settingsDialog", u"Config", None))
        self.addConfigBtn.setText(QCoreApplication.translate("settingsDialog", u"\u2795", None))
        self.renameConfigBtn.setText(QCoreApplication.translate("settingsDialog", u"\u270e", None))
        self.deleteConfigBtn.setText(QCoreApplication.translate("settingsDialog", u"\u2573", None))
        self.configNameLabel.setText(QCoreApplication.translate("settingsDialog", u"New config", None))
        self.saveConfigNameBtn.setText(QCoreApplication.translate("settingsDialog", u"OK", None))
        self.defaultValuesLabel.setText(QCoreApplication.translate("settingsDialog", u"Config values", None))
        self.replaceWithCurrentValuesBtn.setText(QCoreApplication.translate("settingsDialog", u"Replace with current values", None))
        self.sensorGpioLabel.setText(QCoreApplication.translate("settingsDialog", u"Sensor GPIO Pins", None))
        self.s1Label.setText(QCoreApplication.translate("settingsDialog", u"S1", None))
        self.s3Label.setText(QCoreApplication.translate("settingsDialog", u"S3", None))
        self.s2Label.setText(QCoreApplication.translate("settingsDialog", u"S2", None))
        self.s4Label.setText(QCoreApplication.translate("settingsDialog", u"S4", None))
        self.cancelBtn.setText(QCoreApplication.translate("settingsDialog", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("settingsDialog", u"\U0001f4be Save", None))
    # retranslateUi

