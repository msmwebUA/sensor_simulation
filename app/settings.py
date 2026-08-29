import os
import messages

class Settings:
  def __init__(self):
    self.settings_file = "settings.json"
    self.saved_settings, self.current_settings = self.loadSettings()
    self.current_config_id = self.getCurrentConfigId(self.saved_settings)
  
  def loadSettings(self) -> dict:
    if not os.path.exists(self.settings_file):
      with open(self.settings_file, "w", encoding="utf-8") as f:
        json.dump(self.createConfigExample(), f, indent=2)
        messages.ConsoleMessage.append(f"Settings file created: {self.settings_file}")
    try:
      settings = {}
      with open(self.settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        messages.ConsoleMessage.append(f"Settings loaded from file {self.settings_file}")
        return settings
    except FileNotFoundError:
      messages.ConsoleMessage.append(f"Settings file not found: {self.settings_file}")
    except json.JSONDecodeError:
      messages.ConsoleMessage.append(f"Settings file {self.settings_file} corrupted")
    except Exception as e:
      messages.ConsoleMessage.append(f"Error loading settings: {e}")
    finally:
      return settings
  
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
  
  def validateSettings(self, settings: dict) -> bool:
    return False

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
      messages.showAlert(self, "Error", "Invalid settings", "critical")
      # TODO prevent dialog closing

  def getCurrentConfigId(self, settings: dict) -> str:
    for key, value in settings.items():
      if value["current"]:
        return key
  
  def setCurrentConfigId(self, settings: dict, config_id: str) -> None:
    settings[config_id]["current"] = True

  def createConfigExample(self) -> dict:
    return {
      "1": {
        "name": "Config 1",
        "current": true,
        "main_block": {
          "rpm": 20
        },
        "sensors": [
          {
            "id": 1,
            "gpio": 27,
            "rpm": 10,
            "coefficient": "1/2"
          },
          {
            "id": 2,
            "gpio": 22,
            "rpm": 10,
            "coefficient": "1/2"
          },
          {
            "id": 3,
            "gpio": 23,
            "rpm": 10,
            "coefficient": "1/2"
          },
          {
            "id": 4,
            "gpio": 24,
            "rpm": 10,
            "coefficient": "1/2"
          }
        ]
      }
    }