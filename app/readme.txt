================================================================================
3K Sensor Simulation App
Version: 1.0 092026
Sergii Mishchaniuk
================================================================================

--------------------------------------------------------------------------------
FEATURES
--------------------------------------------------------------------------------
- Simulate 4 independent rotational sensors using Raspberry Pi GPIO output pins
  (via gpiozero library), toggling each pin on/off (high/low) at a frequency derived from RPM settings.
  Max frequency (RPM per sensor) depends on hardware speed. 
- Pause and resume each of the 4 sensors individually while the simulation
  is running.
- Two RPM modes:
    * Automatic: set a "Main Block RPM" and a coefficient (x/y) per sensor;
      each sensor's RPM is calculated automatically.
    * Manual: set each sensor's RPM directly; the coefficient is calculated
      automatically from the main block RPM.
- Create, rename, and delete configurations from the Settings dialog.
- Save configurations to a local settings.json file for reuse between runs.
- Console log of simulation and configuration events.

--------------------------------------------------------------------------------
SYSTEM REQUIREMENTS
--------------------------------------------------------------------------------
- Raspberry Pi (or compatible board) with at least 4 accessible GPIO pins and ARM processor.

Application successfully tested on RPI3 model B v.1.2. 1Gb RAM with OS Linux Debian Bookworm.

--------------------------------------------------------------------------------
DEFAULT SETTINGS
--------------------------------------------------------------------------------
If no settings.json file is found, the application
automatically creates one with a single default configuration:

    Config name:      DefaultConfig1
    Main block RPM:   100
    Sensor 1:         GPIO 27, RPM 50, coefficient 1/2
    Sensor 2:         GPIO 22, RPM 50, coefficient 1/2
    Sensor 3:         GPIO 23, RPM 50, coefficient 1/2
    Sensor 4:         GPIO 24, RPM 50, coefficient 1/2

This configuration is also used as a starting point when a new
configuration is created from the Settings dialog.

--------------------------------------------------------------------------------
EXAMPLE OF CONFIG (settings.json)
--------------------------------------------------------------------------------
{
  "1": {
    "name": "Config1",
    "current": true,
    "main_block": {
      "rpm": 100
    },
    "sensors": [
      { "id": 1, "gpio": 27, "rpm": 50, "coefficient": "1/2" },
      { "id": 2, "gpio": 22, "rpm": 50, "coefficient": "1/2" },
      { "id": 3, "gpio": 23, "rpm": 50, "coefficient": "1/2" },
      { "id": 4, "gpio": 24, "rpm": 50, "coefficient": "1/2" }
    ]
  }
}

Notes:
- Top-level key ("1", "2", ...) - configuration ID. Must be a
  positive integer written as a string.
- Exactly one configuration must have "current": true. It means that this configuration will be used as default at program start.
- Exactly four sensors are required per configuration, with unique IDs 1-4
  and unique GPIO pins.

Program validate settings.json each time at program start.

--------------------------------------------------------------------------------
LIMITATIONS
--------------------------------------------------------------------------------
- Exactly 4 sensors per configuration are supported; this is fixed and
  cannot be changed from the UI.
- GPIO pin choice is restricted to a fixed set of known-safe pins
  (4, 5, 6, 12, 13, 16-27); other pins cannot be assigned.
- RPM values must be integers between 1 and 10000. Max frequency (RPM per sensor) 
  depends on hardware speed.
- Coefficients must be entered as a simple fraction "x/y" (positive
  integers only, y not equal to 0). When using automatic mode, the main
  block RPM multiplied by the coefficient must produce a whole number.
- Configuration names must be unique and alphanumeric only (letters and digits, no
  spaces or symbols) and no longer than 20 characters.
- The application is intended for simulation/testing purposes; sensor
  RPM values do not reflect real-world sensor readings.
================================================================================
