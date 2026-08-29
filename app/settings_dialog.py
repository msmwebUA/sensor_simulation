from PySide6.QtWidgets import QDialog
from ui_settings_dialog import Ui_settingsDialog
import messages

class SettingsDialog(QDialog, Ui_settingsDialog):
  def __init__(self, settings_obj, parent=None):
    super().__init__(parent)
    self.setupUi(self)

    # Settings
    self.settings_obj = settings_obj, 
    self.modified_settings = self.settings_obj.saved_settings # modified settings dict for keeping changes made on the dialog page

    # show or hide items
    self.showConfigItems()
    if self.settings_obj.current_config_id == 0:
      self.editConfigNameBtn.setVisible(False)
      self.deleteConfigBtn.setVisible(False)

    # Connect methods to events
    self.buttonBox.accepted.connect(self.settings_obj.saveSettings)
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
      messages.showAlert(self, "Error", "Cannot create or update config name", "critical")
  
  def deleteConfig(self) -> None:
    # TODO delete config from self.modified_settings
    # TODO consider to ask for confirmation
    pass

  # VALUES AND PAGE ITEMS

  def replaceValues(self) -> None:
    # TODO replace saved values with current in self.modified_settings
    pass
  
  def setPageItems(self, settings) -> None:
    # TODO parse dict with settings and set values to page items based on config id
    pass




  # self.buttonBox.clicked.connect(self.handleButtonBoxClick)
  # def handleButtonBoxClick(self, button) -> None:
  #   clicked_button = self.buttonBox.standardButton(button)
  #   if clicked_button == self.buttonBox.Save:
  #     self.saveSettings()
  #   elif clicked_button == self.buttonBox.Cancel:
  #     self.setDefaultValuesToMainWindow()