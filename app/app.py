# import UI
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Qt, QElapsedTimer, QDateTime
from ui import Ui_MainWindow
from settings_dialog import SettingsDialog
from settings import Settings
import messages
import copy
from math import gcd

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
    # self.setCursor(Qt.CursorShape.BlankCursor)
    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)

    # set widget for console messages
    messages.ConsoleMessage.setWidget(self.consoleText)
    # print version to console
    messages.ConsoleMessage.append(f"3K Sensor simulation: version {VERSION}")
    
    # init objects and vars
    self.settings_obj = Settings()
    if not self.settings_obj.saved_settings:
      messages.showAlert(self, "Error", f"Cannot run program. Settings file '{self.settings_obj.settings_file}' corrupted. Fix invalid values.", "critical")
      # close app
      sys.exit(1)
    self.elapsed_timer = QElapsedTimer()

    self.channels = {}
    self.channels_active = {}
    self.channels_half_period = {}

    # show, hide or set items
    self.sensorControlButtons = [self.controlS1Btn, self.controlS2Btn, self.controlS3Btn, self.controlS4Btn]
    self.mainBlockItems = [[self.mainBlockRpm, "mainBlockRpm"]]
    self.coefficientItems = [[self.sensor1Coefficient, 1], [self.sensor2Coefficient, 2], [self.sensor3Coefficient, 3], [self.sensor4Coefficient, 4]]
    self.sensorRpmItems = [[self.sensor1Rpm, 1], [self.sensor2Rpm, 2], [self.sensor3Rpm, 3], [self.sensor4Rpm, 4]]
    self.hideSensorControlButtons()
    self.setPageItemsValues(self.settings_obj.saved_settings)
    self.manualRpmCheckBoxChanged(self.manualRpmCheckBox.checkState())

    # connect slots (methods) to buttons on signals (events)
    self.settingsBtn.clicked.connect(self.showSettingsDialog)
    self.resetConfigBtn.clicked.connect(self.resetConfig)
    self.configComboBox.currentIndexChanged.connect(self.configComboBoxChanged)
    self.manualRpmCheckBox.stateChanged.connect(self.manualRpmCheckBoxChanged)
    self.clearConsoleBtn.clicked.connect(messages.ConsoleMessage.clear)
    self.simulationBtn.clicked.connect(self.simulation)
    self.controlS1Btn.clicked.connect(lambda _: self.controlSensor(1))
    self.controlS2Btn.clicked.connect(lambda _: self.controlSensor(2))
    self.controlS3Btn.clicked.connect(lambda _: self.controlSensor(3))
    self.controlS4Btn.clicked.connect(lambda _: self.controlSensor(4))
    for item in [self.mainBlockItems, self.sensorRpmItems]:
      for subitem in item:
        subitem[0].valueChanged.connect(self.pageItemsChangedManually)
    for item in self.coefficientItems:
      item[0].editingFinished.connect(self.pageItemsChangedManually)

    # flags
    self.manual_mode = False
    self.simulationStarted = False
    self.block_page_items_changed = False

    # add listener to program exit and purge channels
      # self.purgeChannels()

  # SIMULATION
  def simulation(self) -> None:
    # start or stop simulation
    self.simulationStarted = not self.simulationStarted
    if self.simulationStarted:
      self.simulationStart()
    else:
      self.simulationStop()

  def simulationStart(self) -> None:
    # start if current config valid
    if self.settings_obj.validateSettings(self.settings_obj.current_settings):
      self.disablePageItems()
      self.simulationBtn.setText("⏹️ Stop simulation")
      self.channels_active = {
        1: [True, self.controlS1Btn],
        2: [True, self.controlS2Btn],
        3: [True, self.controlS3Btn],
        4: [True, self.controlS4Btn]
      }
      self.elapsed_timer.start()
      sensors = self.settings_obj.current_settings[self.settings_obj.getCurrentConfigId(self.settings_obj.current_settings)]["sensors"]
      try:
        for sensor in sensors:
          rpm = sensor["rpm"]
          channel = DigitalOutputDevice(sensor["gpio"], active_high=True, initial_value=True)
          # keep gpio pin's mode as object otherwise it will be collected to garbage in next iteration
          self.channels[sensor["id"]] = channel
          # frequency
          frequency = rpm / 60.0
          # time for active low and high
          half_period = (1.0 / frequency) / 2.0
          self.channels_half_period[sensor["id"]] = half_period
          # run built-in blink method, infinite
          # RPI LOW -> pin closed to GND
          # RPI HIGH -> pin switched to 
          channel.blink(on_time=half_period, off_time=half_period, background=True)
          messages.ConsoleMessage.append(f"[sensor{sensor['id']}], GPIO{sensor['gpio']} -> {rpm} RPM (half period: {half_period:.4f} s)") 
      except Exception as e:
        messages.ConsoleMessage.append(f"Failed to start simulation: {e}")
        messages.showAlert(self, "Error", f"Failed to start simulation: {e}", "critical")
        self.simulationStop()   # roll back to a consistent state instead of leaving buttons hidden
        self.simulationStarted = False
        return
      self.showSensorControlButtons()
    else:
      messages.ConsoleMessage.append("Cannot start simulation: Invalid settings")
      messages.showAlert(self, "Error", "Cannot start simulation: Invalid settings", "critical")

  def simulationStop(self) -> None:
    elapsed_ms = self.elapsed_timer.elapsed()
    self.elapsed_timer.invalidate()
    self.purgeChannels()
    self.channels_half_period = {}
    self.hideSensorControlButtons()
    self.unablePageItems()
    self.simulationBtn.setText("▶️ Start simulation")
    messages.ConsoleMessage.append(f"Simulation stopped. Elapsed time: {self.formatElapsedTime(elapsed_ms)}")
  
  def purgeChannels(self) -> None:
    for channel in self.channels.values():
      channel.close()

  def controlSensor(self, sensor: int) -> None:
    self.channels_active[sensor][0] = not self.channels_active[sensor][0]
    if self.channels_active[sensor][0]:
      half_period = self.channels_half_period[sensor]
      self.channels[sensor].blink(on_time=half_period, off_time=half_period, background=True)
      messages.ConsoleMessage.append(f"Sensor{sensor} -> Active")
      self.channels_active[sensor][1].setText(f"⏹️ Stop S{sensor}")
    else:
      self.channels[sensor].off()
      messages.ConsoleMessage.append(f"Sensor{sensor} -> Paused")
      self.channels_active[sensor][1].setText(f"▶️ Start S{sensor}")

  def formatElapsedTime(self, elapsed_ms: int) -> str:
    total_seconds = elapsed_ms // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    millis = elapsed_ms % 1000
    if hours:
      return f"{hours}h {minutes}m {seconds}s"
    elif minutes:
      return f"{minutes}m {seconds}s"
    else:
      return f"{seconds}.{millis:03d}s"

  def resetConfig(self) -> None:
    current_config_id = self.settings_obj.getCurrentConfigId(self.settings_obj.current_settings)
    if self.configComboBox.currentData() == current_config_id:
      update_success = self.settings_obj.updateCurrentSettings(self.settings_obj.saved_settings)
      if update_success:
        self.block_page_items_changed = True
        try:
          self.setPageItemsValues(self.settings_obj.current_settings, False) # False -> don't update combobox
          self.simulationBtn.setEnabled(True)
        finally:
          self.block_page_items_changed = False
      else:
        messages.showAlert(self, "Error", f"Cannot reset config. Saved settings corrupted or current config not found", "critical")
        messages.ConsoleMessage.append(f"Cannot reset config. Saved settings corrupted or current config not found")
    else:
      messages.ConsoleMessage.append(f'Cannot reset config.  Status "Current" of config on the page is different from saved settings')

  # PAGE ITEMS

  def getPageItemsValues(self) -> dict:
    # dicts to map id to page item
    coefficient_by_id = {sensor_id: page_item for page_item, sensor_id in self.coefficientItems}
    rpm_by_id = {sensor_id: page_item for page_item, sensor_id in self.sensorRpmItems}
    return {
      self.configComboBox.currentData(): {
        "name": self.configComboBox.currentText(),
        "current": True,
        "main_block": {
          "rpm": self.mainBlockRpm.value()
        },
        "sensors": [
          {
            "id": sensor["id"],
            "gpio": sensor["gpio"],
            "rpm": rpm_by_id[sensor["id"]].value(),
            "coefficient": coefficient_by_id[sensor["id"]].text()
          }
          for sensor in self.settings_obj.current_settings[self.settings_obj.getCurrentConfigId(self.settings_obj.current_settings)]["sensors"]
        ]
      }
    }

  def setPageItemsValues(self, settings: dict, update_combobox: bool = True) -> None:
    current_config_id = self.settings_obj.getCurrentConfigId(self.settings_obj.current_settings)
    # update config combobox
    if update_combobox:
      self.configComboBox.clear()
      for key, value in settings.items():
        self.configComboBox.addItem(value["name"], key)
      index = self.configComboBox.findData(current_config_id)
      if index != -1:
        self.configComboBox.setCurrentIndex(index)
      else:
        self.configComboBox.setCurrentIndex(0)
        messages.ConsoleMessage.append(f"Current config with ID {current_config_id} not found on the page, using first config")
        messages.showAlert(self, "Error", f"Current config with ID {current_config_id} not found on the page, using first config", "critical")
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

  def pageItemsChangedManually(self) -> None:
    if self.block_page_items_changed:
      return
    values = self.getPageItemsValues()
    if not self.settings_obj.validateSettings(values):
      self.simulationBtn.setEnabled(False)
      return
    edited_values = self.countRevolutions(values)
    if not edited_values:
      self.simulationBtn.setEnabled(False)
      return
    if self.settings_obj.updateCurrentSettings(edited_values):
      self.block_page_items_changed = True
      try:
        self.setPageItemsValues(self.settings_obj.current_settings, False) # false -> don't update combobox
        self.simulationBtn.setEnabled(True)
      finally:
        self.block_page_items_changed = False
    else:
      self.simulationBtn.setEnabled(False)

  def countRevolutions(self, values: dict) -> dict:
    edited_values = copy.deepcopy(values)
    errors = []
    for config in edited_values.values():
      main_block = config.get("main_block", {})
      main_block_rpm = main_block.get("rpm", 0)
      for sensor in config.get("sensors", []):
        # calculate sensor rpm from main block rpm and coefficient
        if self.manual_mode:
          sensor_rpm = sensor.get("rpm", 0)
          if main_block_rpm == 0:
            errors.append("Cannot calculate coefficient when main block RPM is zero")
          else:
            # simplify fraction using gcd
            divisor = gcd(abs(sensor_rpm), abs(main_block_rpm))
            # calculate coefficient
            numerator = sensor_rpm // divisor
            denominator = main_block_rpm // divisor
            # keep denominator positive
            if denominator < 0:
              numerator *= -1
              denominator *= -1
            # write result
            sensor["coefficient"] = f"{numerator}/{denominator}"
        # calculate coefficient from sensor rpm and main block rpm
        else:
          coefficient = sensor.get("coefficient", "0/1")
          try:
            numerator, denominator = map(int, coefficient.split("/"))
            if denominator == 0:
              errors.append("Coefficient denominator cannot be zero")
              continue
            result = main_block_rpm * numerator
            if result % denominator != 0:
              errors.append(f"Sensor RPM must be an integer. {main_block_rpm} * {coefficient} does not produce an integer RPM")
              continue
            sensor["rpm"] = result // denominator
          except (ValueError, AttributeError):
            errors.append(f"Invalid coefficient format: {coefficient}. Expected format: x/y") 
    if errors:
      errors_set = set(errors)
      for error in errors_set:
        messages.ConsoleMessage.append(error)
      # messages.showAlert(self, "Warning", "Cannot calculate values. Check console for details", "warning")
      errors.clear()
      errors_set.clear()
      return None
    else:
      return edited_values
  
  def manualRpmCheckBoxChanged(self, state) -> None:
    if state == Qt.CheckState.Checked.value:
      self.manual_mode = True
      for item in self.coefficientItems:
        item[0].setEnabled(False)
      for item in self.sensorRpmItems:
        item[0].setEnabled(True)
    else:
      self.manual_mode = False
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
    self.settingsBtn.setEnabled(False)
    self.resetConfigBtn.setEnabled(False)
    self.clearConsoleBtn.setEnabled(False)

  def unablePageItems(self) -> None:
    self.configComboBox.setEnabled(True)
    for item in self.mainBlockItems:
      item[0].setEnabled(True)
    self.manualRpmCheckBox.setEnabled(True)
    if self.manual_mode:
      for item in self.coefficientItems:
        item[0].setEnabled(False)
      for item in self.sensorRpmItems:
        item[0].setEnabled(True)
    else:
      for item in self.coefficientItems:
        item[0].setEnabled(True)
      for item in self.sensorRpmItems:
        item[0].setEnabled(False)
    self.settingsBtn.setEnabled(True)
    self.resetConfigBtn.setEnabled(True)
    self.clearConsoleBtn.setEnabled(True)

  def hideSensorControlButtons(self) -> None:
    for btn in self.sensorControlButtons:
      btn.setVisible(False)
  
  def showSensorControlButtons(self) -> None:
    for btn in self.sensorControlButtons:
      btn.setVisible(True)

  def configComboBoxChanged(self) -> None:
    config_id = self.configComboBox.currentData()
    if config_id:
      self.settings_obj.setCurrentConfigId(config_id, self.settings_obj.current_settings)
      self.block_page_items_changed = True
      try:
        self.setPageItemsValues(self.settings_obj.current_settings, False) # false -> don't update combobox
        self.simulationBtn.setEnabled(True)
      finally:
        self.block_page_items_changed = False

  # DIALOG

  def showSettingsDialog(self) -> None:
    dialog = SettingsDialog(self.settings_obj)
    if dialog.exec() == QDialog.Accepted:
      self.block_page_items_changed = True
      try:
        self.setPageItemsValues(self.settings_obj.current_settings, True) # true -> also update combobox
        self.simulationBtn.setEnabled(True)
      finally:
        self.block_page_items_changed = False
  
  # CUSTOM CLOSE

  def closeEvent(self, event: QCloseEvent) -> None:
    if self.simulationStarted:
      stay_in_program = messages.showConfirmation(self, "Simulation running", "Simulation is currently running. Do you want to stay in the program?")
      if stay_in_program:
        event.ignore()
        return
      self.simulationStop()

    has_unsaved_changes = (self.settings_obj.current_settings != self.settings_obj.saved_settings)

    if has_unsaved_changes:
      save_changes = messages.showConfirmation(self, "Save changes?", "Changes to configuration were made or default config was changed. Save changes?")
      if save_changes:
        if not self.settings_obj.saveSettings(self.settings_obj.current_settings):
          event.ignore()
          return

    event.accept()
