# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP3428
# This code is designed to work with the MCP3428_I2CADC I2C Mini Module available from ControlEverything.com.
# https://shop.controleverything.com/collections/4-20-ma-current-loop-input
import smbus
import time
DL = 0
DL1 = 0.01
# Get I2C bus
bus = smbus.SMBus(1)

# MCP3428 address, 0x68(104)
# Send configuration command
#               0x10(16)Continuous conversion mode, Channel-1, 12-bit Resolution

while True:
        bus.write_byte(0x68, 0x10)
        time.sleep(DL1)
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
        print "Current Output channel 1 : %.2f" %current
        time.sleep(DL)

####### channel 2
        bus.write_byte(0x68, 0x30)
        time.sleep(DL1)
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
        print "Current Output channel 2 : %.2f" %current
        time.sleep(DL)
############ channel 3
        bus.write_byte(0x68, 0x50)
        time.sleep(DL1)
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
        print "Current Output channel 3 : %.2f" %current
        time.sleep(DL)
####### channel 4
        bus.write_byte(0x68, 0x70)
        time.sleep(DL1)
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
        print "Current Output channel 4 : %.2f" %current
        time.sleep(DL)
