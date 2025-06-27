#!
#
#
import spidev
import time

# Define ADC channel and ACS712 parameters
ACS_CHANNEL = 0  # Channel number on the ADC (e.g., SPI channel 0)
ACS_SENSITIVITY = 0.185  # Sensitivity of the ACS712 (V/A) - check datasheet for your specific model (e.g., 0.185 for 5A, 0.1 for 20A, 0.066 for 30A)
VCC = 3.3  # Voltage of the Raspberry Pi's 3.3V rail. If using an external power supply, adjust this value and the zero_amp_voltage
ZERO_AMP_VOLTAGE = VCC / 2  # The voltage output by the ACS712 when no current is flowing (ideally VCC/2)
# Note: If you are using an external 5V power supply for the ACS712, and the Raspberry Pi's VCC is 3.3V, you may need to adjust these values accordingly.
# You can measure the actual zero_amp_voltage with a multimeter when there is no current flowing through the sensor.

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # bus, device (e.g., CE0)
spi.max_speed_hz = 1000000  # Set SPI speed (adjust as needed)


def read_adc(channel):
    """Reads a value from the specified ADC channel."""
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


def calculate_current(adc_value):
    """Converts the ADC value to a current reading."""
    voltage = (adc_value * VCC) / 1023.0  # Convert ADC value to voltage
    current = (voltage - ZERO_AMP_VOLTAGE) / ACS_SENSITIVITY
    return current


try:
    while True:
        # Read data from the sensor
        adc_value = read_adc(ACS_CHANNEL)

        # Calculate the current
        current = calculate_current(adc_value)

        # Print the results
        print(f"ADC Value: {adc_value}, Current: {current:.2f} A")

        time.sleep(0.1)  # Sample rate

except KeyboardInterrupt:
    print("Exiting program")
finally:
    spi.close()
