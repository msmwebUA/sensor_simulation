import json
from gpiozero import DigitalOutputDevice

settings_file = "settings.json"

def main():
    consoleMessage("Running simulation...")
    # load settings
    try:
        with open(settins_file, "r", encoding="utf-8") as f:
            settings = json.load(f)
        consoleMessage(f"Settings loaded from file {settings_file}")
    except FileNotFoundError:
        consoleMessage(f"Settings file not found: {settings_file}")
    except json.JSONDecodeError:
        consoleMessage(f"Settings file {settings_file} corrupted")
    except Exception as e:
        consoleMessage(f"Error loading settings: {e}")

    channels = {}
    # sensors as dict
    sensors = settings["sensors"]
    for sensor in sensors:
        rpm = sensor["rpm"]
        channel = DigitalOutputDevice(sensor["gpio"], active_high=True, initial_value=True)
        # keep gpio pin's mode as object otherwise it will be collected to garbage in next iteration
        channels[sensor["id"]] = channel
        if rpm > 0:
            frequency = rpm / 60.0
            # time for active low and high
            half_period = (1.0 / frequency) / 2.0
            # run built-in blink method, infinite
            # RPI LOW -> pin closed to GND
            # RPI HIGH -> pin switched to 
            channel.blink(on_time=half_period, off_time=half_period, background=True)
            consoleMessage(f"[sensor{sensor['id']}], GPIO{pin} -> {rpm} RPM (half period: {half_period:.4f} s)")
        else:
            channel.off()
            consoleMessage(f"[sensor{sensor['id']}], GPIO{pin} -> Stopped (0 RPM)")

        # for channel in channels.values():
        #     channel.close()

if __name__ == "__main__":
    main()