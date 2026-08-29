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
    self.hideSensorControlButtons()
    self.setPageItems(self.settings_obj.saved_settings)

    # connect slots (methods) to buttons on signals (events)
    self.simulationBtn.clicked.connect(self.simulation)
    self.settingsBtn.clicked.connect(self.showSettingsDialog)
    self.manualRpmCheckBox.clicked.connect(self.manualRpmCheckBoxChanged)
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
  
  def purgeChannels(self) -> None:
    for channel in self.channels.values():
      channel.close()

  def controlSensor(self, sensor: int) -> None:
    pass
    pass

  # PAGE ITEMS

  def setPageItems(self, settings: dict) -> None:
    # TODO set values from dict into page items (config "current" key in dict is true)
    pass
    # self.current_config_id = 1

  def countRevolutions(self) -> None:
    pass
  
  def manualRpmCheckBoxChanged(self, state) -> None:
    if state == Qt.CheckState.Checked:
      pass
    elif state == Qt.CheckState.Unchecked:
      pass
  
  def hideSensorControlButtons(self) -> None:
    self.controlS1Btn.setVisible(False)
    self.controlS2Btn.setVisible(False)
    self.controlS3Btn.setVisible(False)
    self.controlS4Btn.setVisible(False)
  
  def showSensorControlButtons(self) -> None:
    self.controlS1Btn.setVisible(True)
    self.controlS2Btn.setVisible(True)
    self.controlS3Btn.setVisible(True)
    self.controlS4Btn.setVisible(True)

  # DIALOG

  def showSettingsDialog(self) -> None:
    dialog = SettingsDialog(self.settings_obj)

