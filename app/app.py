# import UI
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt, QElapsedTimer, QDateTime
from ui import Ui_MainWindow
from settings_dialog import SettingsDialog
from settings import Settings
import messages

import json
from gpiozero import DigitalOutputDevice

VERSION = "1.0"

# now = QDateTime.currentDateTime()

class App(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)

    # maximized window
    self.showMaximized()
    # hide cursor
    self.setCursor(Qt.CursorShape.BlankCursor)
    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)
    
    # init objects
    self.settings_obj = Settings()
    messages.ConsoleLogger.setWidget(self.consoleText)

    # show, hide or set items
    self.sensorControlButtons = [self.controlS1Btn, self.controlS2Btn, self.controlS3Btn, self.controlS4Btn]
    self.mainBlockItems = [[self.mainBlockRpm, "mainBlockRpm"]]
    self.coefficientItems = [[self.sensor1Coefficient, 1], [self.sensor2Coefficient, 2], [self.sensor3Coefficient, 3], [self.sensor4Coefficient, 4]]
    self.sensorRpmItems = [[self.sensor1Rpm, 1], [self.sensor2Rpm, 2], [self.sensor3Rpm, 3], [self.sensor4Rpm, 4]]
    self.hideSensorControlButtons()
    self.setPageItems(self.settings_obj.saved_settings)

    # connect slots (methods) to buttons on signals (events)
    self.settingsBtn.clicked.connect(self.showSettingsDialog)
    self.configComboBox.currentIndexChanged.connect(self.configComboBoxChanged)
    self.manualRpmCheckBox.clicked.connect(self.manualRpmCheckBoxChanged)
    self.simulationBtn.clicked.connect(self.simulation)
    self.controlS1Btn.clicked.connect(lambda _, arg="1": self.controlSensor(arg))
    self.controlS2Btn.clicked.connect(lambda _, arg="2": self.controlSensor(arg))
    self.controlS3Btn.clicked.connect(lambda _, arg="3": self.controlSensor(arg))
    self.controlS4Btn.clicked.connect(lambda _, arg="4": self.controlSensor(arg))


    # init elapsed timer
    self.elapsed_timer = QElapsedTimer()

    # print version to console
    messages.ConsoleMessage.append(f"3K Sensor simulation: version {VERSION}")

    # add listener to program exit and purge channels
      # self.purgeChannels()

  # SIMULATION

  def simulationStart(self) -> None:
    self.elapsed_timer.start()
    self.channels = {}
    # sensors as dict
    if self.settings_obj.validateSettings(self.settings_obj.current_settings):
      self.disablePageItems()
      sensors = self.settings_obj.current_settings[self.settings_obj.current_config_id]["sensors"]
      for sensor in sensors:
        rpm = sensor["rpm"]
        channel = DigitalOutputDevice(sensor["gpio"], active_high=True, initial_value=True)
        # keep gpio pin's mode as object otherwise it will be collected to garbage in next iteration
        self.channels[sensor["id"]] = channel
        if rpm > 0:
          frequency = rpm / 60.0
          # time for active low and high
          half_period = (1.0 / frequency) / 2.0
          # run built-in blink method, infinite
          # RPI LOW -> pin closed to GND
          # RPI HIGH -> pin switched to 
          channel.blink(on_time=half_period, off_time=half_period, background=True)
          messages.ConsoleMessage.append(f"[sensor{sensor['id']}], GPIO{pin} -> {rpm} RPM (half period: {half_period:.4f} s)")
        else:
          channel.off()
          messages.ConsoleMessage.append(f"[sensor{sensor['id']}], GPIO{pin} -> Stopped (0 RPM)")
      self.showSensorControlButtons()
    else:
      messages.ConsoleMessage.append("Cannot start simulation: Invalid settings")

  def simulationStop(self) -> None:
    self.elapsed_timer.stop()
    self.purgeChannels()
    self.hideSensorControlButtons()
    self.unablePageItems()
  
  def purgeChannels(self) -> None:
    for channel in self.channels.values():
      channel.close()

  def controlSensor(self, sensor: int) -> None:
    pass
    pass

  # PAGE ITEMS

  def getPageItems(self) -> dict:
    values = {}
    for main_block in self.mainBlockItems:
      values[main_block[1]] = main_block[0].value()
    for coefficient in self.coefficientItems:
      values[f"sensor{coefficient[1]}Coefficient"] = coefficient[0].text()
    for rpm in self.sensorRpmItems:
      values[f"sensor{rpm[1]}Rpm"] = rpm[0].value()
    return values

  def setPageItems(self, settings: dict) -> None:
    current_config_id = self.settings_obj.current_config_id
    # config combobox
    self.configComboBox.clear()
    for key, value in settings.items():
      self.configComboBox.addItem(value["name"], key)
    self.configComboBox.setCurrentIndex(current_config_id)
    # main block
    for item in self.mainBlockItems:
      item[0].setValue(settings[current_config_id]["main_block"]["rpm"])
    # sensors
    sensors = settings[current_config_id]["sensors"]
    for sensor in sensors:
      # coefficients
      for item in self.coefficientItems:
        if item[1] == sensor["id"]:
          item[0].setText(sensor["coefficient"])
      # rpm
      for item in self.sensorRpmItems:
        if item[1] == sensor["id"]:
          item[0].setValue(sensor["rpm"])
    # uncheck manual rpm checkbox
    self.manualRpmCheckBox.setChecked(False)

  def countRevolutions(self) -> None:
    pass
  
  def manualRpmCheckBoxChanged(self, state) -> None:
    if state == Qt.CheckState.Checked:
      for item in self.coefficientItems:
        item[0].setEnabled(False)
      for item in self.sensorRpmItems:
        item[0].setEnabled(True)
    elif state == Qt.CheckState.Unchecked:
      for item in self.coefficientItems:
        item[0].setEnabled(True)
      for item in self.sensorRpmItems:
        item[0].setEnabled(False)
  
  def disablePageItems(self) -> None:
    self.configComboBox.setEnabled(False)
    for item in self.mainBlockItems:
      item[0].setEnabled(False)
    for item in self.coefficientItems:
      item[0].setEnabled(False)
    for item in self.sensorRpmItems:
      item[0].setEnabled(False)
    self.manualRpmCheckBox.setEnabled(False)

  def unablePageItems(self) -> None:
    self.configComboBox.setEnabled(True)
    for item in self.mainBlockItems:
      item[0].setEnabled(True)
    for item in self.coefficientItems:
      item[0].setEnabled(True)
    for item in self.sensorRpmItems:
      item[0].setEnabled(True)
    self.manualRpmCheckBox.setEnabled(True)

  def hideSensorControlButtons(self) -> None:
    for btn in self.sensorControlButtons:
      btn.setVisible(False)
  
  def showSensorControlButtons(self) -> None:
    for btn in self.sensorControlButtons:
      btn.setVisible(True)

  def configComboBoxChanged(self) -> None:
    combobox_config_id = self.configComboBox.currentIndex()
    self.settings_obj.setCurrentConfigId(combobox_config_id)
    self.setPageItems(self.settings_obj.current_settings)

  # DIALOG

  def showSettingsDialog(self) -> None:
    dialog = SettingsDialog(self.settings_obj)
