import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# MCP3428 address, 0x68(104)
# Send configuration command
#               0x10(16)Continuous conversion mode, Channel-1, 12-bit Resolution

while True:
        bus.write_byte(0x68, 0x10)

# MCP3428 address, 0x68(104)
# Read data back from 0x00(0), 2 bytes
# raw_adc MSB, raw_adc LSB
        data = bus.read_i2c_block_data(0x68, 0x00, 2)

# Convert the data to 12-bits
        raw_adc = (data[0] & 0x0F) * 256 + data[1]
        if raw_adc > 2047 :
                raw_adc -= 4095
        current = (raw_adc * 0.022)
# Output data to screen
        print "Current Output : %.2f" %current