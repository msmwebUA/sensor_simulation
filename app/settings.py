import os
import json
import re
import messages

class Settings:
  def __init__(self):
    self.settings_file = "settings.json"
    self.saved_settings, self.current_settings = self.loadSettings()
    self.current_config_id = self.getCurrentConfigId(self.saved_settings)
    self.available_gpio_pins = {4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}
    self.rpm_limit = 10001
  
  def loadSettings(self) -> dict:
    if not os.path.exists(self.settings_file):
      with open(self.settings_file, "w", encoding="utf-8") as f:
        json.dump(self.createConfigExample(), f, indent=2)
        messages.ConsoleMessage.append(f"Settings file created: {self.settings_file}")
    try:
      with open(self.settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        if self.validateSettings(settings):
          messages.ConsoleMessage.append(f"Settings loaded from file {self.settings_file}")
          return settings
        else:
          messages.ConsoleMessage.append(f"Settings file {self.settings_file} corrupted")
          messages.showAlert(self, "Error", "Settings file corrupted", "critical")
          return {}
    except FileNotFoundError:
      messages.ConsoleMessage.append(f"Settings file not found: {self.settings_file}")
    except json.JSONDecodeError:
      messages.ConsoleMessage.append(f"Settings file {self.settings_file} corrupted")
    except Exception as e:
      messages.ConsoleMessage.append(f"Error loading settings: {e}")
    finally:
      return {}
  
  def updateCurrentSettings(self) -> None:
    # TODO update current settings with values changed by user (in main window)
    pass

  def validateSettings(self, settings: dict) -> bool:
    errors = []

    # arg settings must be a non-empty dictionary
    if not isinstance(settings, dict):
      errors.append("Settings must be a dictionary")
    if not settings:
      errors.append("Settings dictionary is empty")

    # validate root keys
    # root_keys = list(data.keys())
    # if any(not isinstance(key, str) or not key.isdigit() for key in root_keys):
    #   errors.append('Root keys in settings must be positive integers represented as strings ("1", "2", "3", etc)')
    ## else:
    ##   key_numbers = [int(key) for key in root_keys]
    ##   if any(number <= 0 for number in key_numbers):
    ##     errors.append('Root keys must start from "1"')
    ##   expected_keys = set(range(1, len(root_keys) + 1))
    ##   if set(key_numbers) != expected_keys:
    ##     errors.append('Root keys in settings must be consecutive and start from "1"')

    # validate configs
    for config_key, config in settings.items():
      location = f'Configuration "{config_key}"'
      if not isinstance(config, dict):
        errors.append(f"{location} must be a dictionary.")
        continue
      # validate name
      name = config.get("name")
      if (not isinstance(name, str) or not name or not name.isalnum()):
       errors.append(f'{location}: "name" must not be empty and must contain letters and digits only')
      # validate current
      if not isinstance(config.get("current"), bool):
        errors.append(f'{location}: "current" must be True or False')
      # validate main block
      main_block = config.get("main_block")
      if not isinstance(main_block, dict):
        errors.append(f'{location}: "main_block" must be a dictionary')
      else:
        main_rpm = main_block.get("rpm")
        if (not isinstance(main_rpm, int) or isinstance(main_rpm, bool) or not 0 < main_rpm < self.rpm_limit):
          errors.append(f'{location}: main_block "rpm" must be an integer between 1 and {self.rpm_limit - 1}')
      # validate sensors
      sensors = config.get("sensors")
      if not isinstance(sensors, list):
        errors.append(f'{location}: "sensors" must be a list')
        continue
      if len(sensors) != 4:
        errors.append(f"{location}: exactly four sensors are required")
      sensor_ids = []
      for index, sensor in enumerate(sensors, start=1):
        sensor_location = (f'{location}, sensor #{index}')
        if not isinstance(sensor, dict):
          errors.append(f"{sensor_location} must be a dictionary")
          continue
        # id
        sensor_id = sensor.get("id")
        if (not isinstance(sensor_id, int) or isinstance(sensor_id, bool) or sensor_id not in {1, 2, 3, 4}):
          errors.append(f'{sensor_location}: "id" must be an integer from 1 to 4')
        else:
          sensor_ids.append(sensor_id)
        # gpio
        gpio = sensor.get("gpio")
        if (not isinstance(gpio, int) or isinstance(gpio, bool) or gpio not in seft.available_gpio_pins):
          errors.append(f'{sensor_location}: "gpio" must be one of the freely available GPIO pins: {str(seft.available_gpio_pins)}')
        # sensor rpm
        sensor_rpm = sensor.get("rpm")
        if (not isinstance(sensor_rpm, int) or isinstance(sensor_rpm, bool) or not 0 < sensor_rpm < self.rpm_limit):
          errors.append(f'{sensor_location}: "rpm" must be an integer between 1 and {self.rpm_limit - 1}')
        # coefficient
        coefficient = sensor.get("coefficient")
        if (not isinstance(coefficient, str) or not re.fullmatch(r"\d+/\d+", coefficient)):
          errors.append(f'{sensor_location}: "coefficient" must be a fraction in the format "x/y"')
        else:
          numerator, denominator = map(int, coefficient.split("/"))
          if denominator == 0:
            errors.append(f'{sensor_location}: coefficient denominator cannot be zero.')
      # check sensor ids are unique and exactly 1, 2, 3, 4
      sensor_ids_set = set(sensor_ids)
      if (len(sensor_ids_set) != 4 or sensor_ids_set != {1, 2, 3, 4}):
        errors.append(f"{location}: sensor IDs must be exactly 1, 2, 3 and 4")
    # validate json
    try:
      json.dumps(settings)
    except (TypeError, ValueError) as e:
      errors.append(f"Configuration cannot be converted to JSON: {e}")
    # show errors and clear list
    if errors:
      for error in errors:
        messages.ConsoleMessage.append(error)
        messages.showAlert(self, "Error", error, "critical")
      errors.clear()
      return False
    # validation passed
    return True

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
  
  def setCurrentConfigId(self, config_id: str) -> None:
    self.current_settings[config_id]["current"] = True
    self.current_config_id = config_id

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