from PySide6.QtWidgets import QDialog
from ui_settings_dialog import Ui_settingsDialog
import messages
import copy

class SettingsDialog(QDialog, Ui_settingsDialog):
  def __init__(self, settings_obj, parent=None):
    super().__init__(parent)
    self.setupUi(self)

    # Settings
    self.settings_obj = settings_obj
    self.modified_settings = copy.deepcopy(self.settings_obj.saved_settings) # modified settings dict for keeping changes made on the dialog page

    # page items
    self.gpio_pins_items = [[self.sensor1Gpio, 1], [self.sensor2Gpio, 2], [self.sensor3Gpio, 3], [self.sensor4Gpio, 4]]
    
    # config combobox
    self.configComboBox.clear()
    for key, value in self.modified_settings.items():
      self.configComboBox.addItem(value["name"], key)
    index = self.configComboBox.findData(self.settings_obj.current_config_id)
    if index != -1:
      self.configComboBox.setCurrentIndex(index)
    else:
      self.configComboBox.setCurrentIndex(0)
      messages.showAlert(self, "Warning", f"Current config {current_config_id} not found in the saved settings, using first config", "warning")

    # show or hide items
    self.showConfigItems()

    # Connect methods to events
    self.configComboBox.currentIndexChanged.connect(self.setPageItems)
    self.addConfigBtn.clicked.connect(lambda _, arg="add": self.showConfigNameForm(arg))
    self.renameConfigBtn.clicked.connect(lambda _, arg="rename": self.showConfigNameForm(arg))
    self.deleteConfigBtn.clicked.connect(self.deleteConfig)
    self.saveConfigNameBtn.clicked.connect(self.manageConfig)
    self.replaceWithCurrentValuesBtn.clicked.connect(self.replaceValues)
    self.cancelBtn.clicked.connect(self.closeDialog)
    self.saveBtn.clicked.connect(self.save)

    # flags
    self.new_config_flag = False
    self.rename_config_flag = False
    
  # MANAGE CONFIG (add, rename, delete)
  
  def hideConfigItems(self) -> None:
    self.configLabel.setVisible(False)
    self.configComboBox.setVisible(False)
    self.addConfigBtn.setVisible(False)
    self.renameConfigBtn.setVisible(False)
    self.deleteConfigBtn.setVisible(False)
    self.configNameLabel.setVisible(True)
    self.configName.setVisible(True)
    self.saveConfigNameBtn.setVisible(True)

  def showConfigItems(self) -> None:
    self.configLabel.setVisible(True)
    self.configComboBox.setVisible(True)
    self.addConfigBtn.setVisible(True)
    if not self.configComboBox.currentData():
      self.renameConfigBtn.setVisible(False)
      self.deleteConfigBtn.setVisible(False)
    else:
      self.renameConfigBtn.setVisible(True)
      self.deleteConfigBtn.setVisible(True)
    self.configNameLabel.setVisible(False)
    self.configName.setVisible(False)
    self.saveConfigNameBtn.setVisible(False)

  def showConfigNameForm(self, flag: str) -> None:
    self.hideConfigItems()
    if flag == "add":
      self.configNameLabel.setValue("New config")
      self.configName.setText("")
      self.new_config_flag = True
      self.rename_config_flag = False
    elif flag == "rename":
      self.configNameLabel.setValue("Rename to")
      self.configName.setText(self.configComboBox.currentText())
      self.rename_config_flag = True
      self.new_config_flag = False
  
  def manageConfig(self) -> None:
    # validate config name
    name = self.configName.text()
    if (not name or not name.isalnum() or len(name) > 20):
      messages.showAlert(self, "Error", f"Config name must: 1. Not be empty; 2. Contain letters and digits only 3. Be max 20 chars)", "critical")
    elif (any(config["name"].strip().lower() == new_name.strip().lower() for config in self.modified_settings.values())):
      messages.showAlert(self, "Error", f"Config name must be unique", "critical")
    else:
      # create or update config
      if self.new_config_flag:
        new_key = str(int(max(self.modified_settings.keys(), key=int)) + 1)
        self.modified_settings.update(self.settings_obj.createConfigExample(new_key, name))
        self.configComboBox.addItem(name, new_key)
        self.configComboBox.setCurrentIndex(self.configComboBox.count() - 1)
        self.setPageItems()
        messages.showAlert(self, "Info", f"New config contains default example values. Consider changing them", "info")
      elif self.rename_config_flag:
        self.modified_settings[self.configComboBox.currentData()]["name"] = name
        self.configComboBox.setItemText(self.configComboBox.currentIndex(), name)
      else:
        messages.showAlert(self, "Error", "Cannot create or update config name", "critical")
    self.configName.setText("")
    self.showConfigItems()
  
  def deleteConfig(self) -> None:
    confirm = messages.showConfirmation(self, "Delete config", "Are you sure you want to delete this config?")
    if confirm:
      self.modified_settings.pop(self.configComboBox.currentData())
      self.configComboBox.removeItem(self.configComboBox.currentIndex())
      if self.comboBox.currentIndex != -1:
        self.modified_settings[self.configComboBox.currentData()]["current"] = True
      else:
        # create new config with default values
        self.modified_settings.update(self.settings_obj.createConfigExample("1", "DefaultConfig1"))
      self.configComboBox.setCurrentIndex(0)
      self.showConfigItems()

  # VALUES AND PAGE ITEMS

  def replaceValues(self) -> None:
    config_id = self.configComboBox.currentData()
    self.modified_settings[config_id] = copy.deepcopy(self.settings_obj.current_settings[config_id])
    self.setPageItems()
  
  def setPageItems(self) -> None:
    config_id = self.configComboBox.currentData()
    self.modified_settings[config_id]["current"] = True
    config = self.modified_settings[config_id]
    sensor_data = [
      f"S{sensor['id']}: coeff. {sensor['coefficient']}, RPM: {sensor['rpm']}"
      for sensor in config["sensors"]
    ]
    text = (
      f"Config name: {config['name']};  Main block RPM: {config['main_block']['rpm']}\n"
      f"Sensors:\n"
      f"\n".join(sensor_data)
    )
    # show list of config values as label
    self.defaultValuesLabel.setText(text)
    # gpio pins
    for sensor in config["sensors"]:
      for item in self.gpio_pins_items:
        if item[1] == sensor["id"]:
          item[0].setValue(sensor["gpio"])

  # DIALOG EVENTS

  def closeDialog(self) -> None:
    self.checkUnsavedChanges()

  # dialog close (os cross button or Alt+F4)
  def closeEvent(self, event: QCloseEvent) -> None:
    self.checkUnsavedChanges()
  
  def checkUnsavedChanges(self) -> None:
    if self.modified_settings != self.settings_obj.saved_settings:
      confirm = messages.showConfirmation(self, "Save changes", "Changes were made. Save them?")
      if confirm:
        self.save()
    self.reject()

  def save(self) -> None:
    if self.settings_obj.saveSettings(self.modified_settings):
      self.accept()
    else:
      messages.showAlert(self, "Error", "Invalid settings. Save operation canceled", "critical")