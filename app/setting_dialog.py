from PySide6.QtWidgets import QDialog
from ui_settings_dialog import Ui_settingsDialog

class SettingsDialog(QDialog, Ui_settingsDialog):
  def __init__(self, saved_settings: dict, current_settings: dict, current_config_id: int, parent=None):
    super().__init__(parent)
    self.setupUi(self)

    # show or hide items
    self.showConfigItems()
    if current_config_id == -1:
      self.editConfigNameBtn.setVisible(False)
      self.deleteConfigBtn.setVisible(False)

    # Settings and values passed from Main Window
    self.saved_settings, self.modified_settings = saved_settings # modified settings dict for keeping changes made on the dialog page
    self.current_settings = current_settings
    self.current_config_id = current_config_id

    # Connect methods to events
    self.buttonBox.accepted.connect(self.saveSettings)
    self.buttonBox.rejected.connect(self.reject)
    self.addConfigBtn.clicked.connect(lambda _, arg="add": self.showConfigNameForm(arg))
    self.renameConfigBtn.clicked.connect(lambda _, arg="rename": self.showEditingForm(arg))
    self.saveConfigNameBtn.clicked.connect(self.manageConfig)

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
    if self.new_config_flag:
      # TODO add new config to self.modified_settings
      pass
    elif self.rename_config_flag:
      # TODO rename config in self.modified_settings
      pass
    else:
      # TODO show error message
      pass
  
  def deleteConfig(self) -> None:
    # TODO delete config from self.modified_settings
    # TODO consider to ask for confirmation
    pass

  # VALUES AND VALIDATIONS

  def replaceValues(self) -> None:
    # TODO replace saved values with current in self.modified_settings
    pass
  
  def parseSettings(self, settings) -> None:
    # TODO parse dict with settings and set values to page items based on config id
    pass

  def validateSettings(self, values: dict) -> bool:
    return False

  # SAVE SETTINGS

  def saveSettings(self) -> None:
    if self.validateSettings(self.modified_settings):
      # TODO fix structure of JSON
      settings_data = {
        "main_block": {"rpm": values["mainBlockRpm"]},
        "sensors": [
          {
            "id": 1,
            "gpio": values["sensor1_gpio"],
            "rpm": values["sensor1_rpm"],
            "coefficient": values["sensor1_coefficient"],
          },
          {
            "id": 2,
            "gpio": values["sensor2_gpio"],
            "rpm": values["sensor2_rpm"],
            "coefficient": values["sensor2_coefficient"],
          },
          {
            "id": 3,
            "gpio": values["sensor3_gpio"],
            "rpm": values["sensor3_rpm"],
            "coefficient": values["sensor3_coefficient"],
          },
          {
            "id": 4,
            "gpio": values["sensor4_gpio"],
            "rpm": values["sensor4_rpm"],
            "coefficient": values["sensor4_coefficient"],
          },
        ],
      }
      # write to json
      with open(self.settings_file, "w", encoding="utf-8") as f:
        json.dump(settings_data, f, indent=2)
      # close dialog as success
      # TODO pass new saved settings to Main Window
      self.accept()
    else:
      # TODO show error message and prevent dialog closing
      pass




  # self.buttonBox.clicked.connect(self.handleButtonBoxClick)
  # def handleButtonBoxClick(self, button) -> None:
  #   clicked_button = self.buttonBox.standardButton(button)
  #   if clicked_button == self.buttonBox.Save:
  #     self.saveSettings()
  #   elif clicked_button == self.buttonBox.Cancel:
  #     self.setDefaultValuesToMainWindow()