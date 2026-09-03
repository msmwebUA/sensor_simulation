import os
import json
import re
import messages
import copy

class Settings:
  def __init__(self):
    self.settings_file = "settings.json"
    self.available_gpio_pins = {4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}
    self.rpm_limit = 10001
    self.saved_settings = self.loadSettings()
    self.current_settings = copy.deepcopy(self.saved_settings)
  
  def loadSettings(self) -> dict:
    if not os.path.exists(self.settings_file):
      with open(self.settings_file, "w", encoding="utf-8") as f:
        json.dump(self.createConfigExample("1", "DefaultConfig1"), f, indent=2)
        messages.ConsoleMessage.append(f"Settings file created: {self.settings_file}")
    try:
      with open(self.settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        if self.validateSettings(settings):
          # first sort sensors by id (if json edited manually)
          for config in settings.values():
            config["sensors"] = sorted(config["sensors"], key=lambda sensor: sensor["id"])
          messages.ConsoleMessage.append(f"Settings loaded from file {self.settings_file}")
          return settings
        else:
          messages.ConsoleMessage.append(f"Settings file {self.settings_file} corrupted")
          messages.showAlert(None, "Error", "Settings file corrupted", "critical")
          return None
    except FileNotFoundError:
      messages.ConsoleMessage.append(f"Settings file not found: {self.settings_file}")
    except json.JSONDecodeError:
      messages.ConsoleMessage.append(f"Settings file {self.settings_file} corrupted")
    except Exception as e:
      messages.ConsoleMessage.append(f"Error loading settings: {e}")
    return None
  
  def updateCurrentSettings(self, config: dict) -> bool:
    # update current settings with values changed by user (in main window)
    try:
      current_config_id = self.getCurrentConfigId(self.current_settings)
      self.current_settings[current_config_id] = config[current_config_id]
      return True
    except Exception as e:
      messages.ConsoleMessage.append(f"Error updating current settings: {e}")
      messages.showAlert(None, "Error", f"{e}", "critical")
      return False

  def validateSettings(self, settings: dict) -> bool:
    errors = []

    # arg settings must be a non-empty dictionary
    if not isinstance(settings, dict):
      errors.append("Settings must be a dictionary")
    if not settings:
      errors.append("Settings dictionary is empty")

    # validate root keys
    root_keys = list(settings.keys())
    if any(not isinstance(key, str) or not key.isdigit() for key in root_keys):
      errors.append('Root keys in settings must be positive integers represented as strings ("1", "2", "3", etc)')

    # validate configs
    config_names = []
    for config_key, config in settings.items():
      location = f'{config["name"]}'
      if not isinstance(config, dict):
        errors.append(f"{location} must be a dictionary.")
        continue
      # validate name
      name = config.get("name")
      if (not isinstance(name, str) or not name or not name.isalnum()):
       errors.append(f'{location}: "name" must not be empty and must contain letters and digits only')
      config_names.append(name)
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
      gpio_pins = []
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
          gpio_pins.append(sensor.get("gpio"))
        # gpio
        gpio = sensor.get("gpio")
        if (not isinstance(gpio, int) or isinstance(gpio, bool) or gpio not in self.available_gpio_pins):
          errors.append(f'{sensor_location}: "gpio" must be one of the available GPIO pins: {str(self.available_gpio_pins)}')
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
      # check gpio pins are unique
      gpio_pins_set = set(gpio_pins)
      if len(gpio_pins_set) != len(gpio_pins):
        errors.append(f"{location}: GPIO pins set must contain 4 unique pins")
    config_names_set = set(config_names)
    if len(config_names_set) != len(config_names):
      errors.append("Configuration names must be unique")
    # validate json
    try:
      json.dumps(settings)
    except (TypeError, ValueError) as e:
      errors.append(f"Configuration cannot be converted to JSON: {e}")
    # show errors and clear list
    if errors:
      for error in errors:
        messages.ConsoleMessage.append(error)
        messages.showAlert(None, "Error", error, "critical")
      errors.clear()
      return False
    # validation passed
    return True

  def saveSettings(self, modified_settings: dict) -> bool:
    if self.validateSettings(modified_settings):
      try:
        # write to json
        with open(self.settings_file, "w", encoding="utf-8") as f:
          json.dump(modified_settings, f, indent=2)
        # replace current and saved settings
        self.saved_settings = copy.deepcopy(modified_settings)
        self.current_settings = copy.deepcopy(modified_settings)
        messages.ConsoleMessage.append(f"Settings saved to file {self.settings_file}")
        return True
      except Exception as e:
        messages.showAlert(None, "Error", f"Error saving settings: {e}", "critical")
    return False

  def getCurrentConfigId(self, settings: dict) -> str:
    for key, value in settings.items():
      if value["current"]:
        return key
    # no current config found, set and return first config
    first_key = next(iter(settings))
    settings[first_key]["current"] = True
    return first_key
  
  def setCurrentConfigId(self, config_id: str, settings: dict) -> None:
    # unset current from other configs
    for config in settings.values():
      config["current"] = False 
    # set current
    settings[config_id]["current"] = True

  def createConfigExample(self, config_id: str, config_name: str) -> dict:
    return {
      config_id: {
        "name": config_name,
        "current": True,
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