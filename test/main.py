# variant with transistor

from gpiozero import DigitalOutputDevice
from signal import pause

# rpm per sensor
RPM_SETTINGS = {
    "s1": 200,   
    "s2": 300, 
    "s3": 400,
    "s4": 500,
}

# gpio
SENSORS = {
    "s1": 27,
    "s2": 22,  
    "s3": 23,  
    "s4": 24,  
}

# keeps sensors as objects
channels = {}

def main():
    print("Running simulation...")
    for sensor, pin in SENSORS.items():
        rpm = RPM_SETTINGS[sensor]
        channel = DigitalOutputDevice(pin, active_high=True, initial_value=True)
        channels[sensor] = channel
        if rpm > 0:
            frequency = rpm / 60.0
            # time for active low and high
            half_period = (1.0 / frequency) / 2.0
            # run built-in blink method, infinite
            # RPI HIGH -> controller's 5V + pull-up closed to GND through transistor
            # RPI LOW -> 5V disconnected from GND
            channel.blink(on_time=half_period, off_time=half_period, background=True)
            print(f"[{sensor}], GPIO{pin} -> {rpm} RPM (half period: {half_period:.4f} s)")
        else:
            channel.off()
            print(f"[{sensor}], GPIO{pin} -> Stopped (0 RPM)")

    print("\nPress Ctrl+C for exit")

    try:
        pause()  # keeps script running
    except KeyboardInterrupt:
        print("\nSimulation stopped")
    finally:
        for channel in channels.values():
            channel.close()

if __name__ == "__main__":
    main()