# import UI
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Qt, QElapsedTimer, QDateTime
from ui import Ui_MainWindow
from settings_dialog import SettingsDialog

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

    # settings file
    self.settings_file = "settings.json"
    # load settings from file
    self.saved_settings, self.current_settings = self.loadSettings()
    # set values from settings
    self.setPageItems(self.saved_settings)

    # show or hide items
    self.hideSensorControlButtons()

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
    self.consoleMessage(f"3K Sensor simulation: version {VERSION}")

    # add listener to program exit and purge channels
      # self.purgeChannels()

  # SIMULATION

  def simulationStart(self) -> None:
    self.elapsed_timer.start()
    self.channels = {}
    # sensors as dict
    current_values = self.getCurrentValues()
    if self.validateValues(values):
      sensors = current_values["sensors"]
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
          self.consoleMessage(f"[sensor{sensor['id']}], GPIO{pin} -> {rpm} RPM (half period: {half_period:.4f} s)")
        else:
          channel.off()
          self.consoleMessage(f"[sensor{sensor['id']}], GPIO{pin} -> Stopped (0 RPM)")
      self.showSensorControlButtons()
    else:
      self.consoleMessage("Cannot start simulation: Invalid values")

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

  def setPageItems(self, values: dict) -> None:
    # TODO set values from dict into page items (config "current" key in dict is true)
    pass

  def countRevolutions(self) -> None:
    pass

  def validateValues(self, values: dict) -> bool:
    return True 
  
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

  # SETTINGS

  def updateCurrentSettings(self) -> None:
    # TODO dict must be with the same structure as settings
    self.current_settings = {
      "mainBlockRpm": self.mainBlockRpm.value(),
      "sensor1_gpio": self.sensor1Gpio.value(),
      "sensor1_rpm": self.sensor1Rpm.value(),
      "sensor1_coefficient": self.sensor1Coefficient.value(),
      "sensor2_gpio": self.sensor2Gpio.value(),
      "sensor2_rpm": self.sensor2Rpm.value(),
      "sensor2_coefficient": self.sensor2Coefficient.value(),
      "sensor3_gpio": self.sensor3Gpio.value(),
      "sensor3_rpm": self.sensor3Rpm.value(),
      "sensor3_coefficient": self.sensor3Coefficient.value(),
      "sensor4_gpio": self.sensor4Gpio.value(),
      "sensor4_rpm": self.sensor4Rpm.value(),
      "sensor4_coefficient": self.sensor4Coefficient.value(),
    }

  def showSettingsDialog(self) -> None:
    dialog = SettingsDialog(self.saved_settings)
    
  def loadSettings(self) -> dict:
    try:
      settings = {}
      with open(self.settins_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        self.consoleMessage(f"Settings loaded from file {self.settings_file}")
        return settings
    except FileNotFoundError:
      self.consoleMessage(f"Settings file not found: {self.settings_file}")
    except json.JSONDecodeError:
      self.consoleMessage(f"Settings file {self.settings_file} corrupted")
    except Exception as e:
      self.consoleMessage(f"Error loading settings: {e}")
    finally:
      return settings

  # MESSAGES

  def consoleMessage(self, message: str) -> None:
    self.consoleText.appendPlainText(message)
  
  def showAlert(self, title: str, text: str, alert_type: str) -> None:
    alert = QMessageBox(self)
    alert.setWindowTitle(title)
    alert.setText(text)
    if alert_type == "info":
      alert.setIcon(QMessageBox.Icon.Information)
    elif alert_type == "warning":
      alert.setIcon(QMessageBox.Icon.Warning)
    elif alert_type == "critical":
      alert.setIcon(QMessageBox.Icon.Critical)
    else:
      alert.setIcon(QMessageBox.Icon.Information)
    alert.setStandardButtons(QMessageBox.StandardButton.Ok)
    alert.exec()