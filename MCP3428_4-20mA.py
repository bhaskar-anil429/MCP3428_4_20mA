# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP3428
# This code is designed to work with the MCP3428_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=MCP3428_I2CADC#tabs-0-product_tabset-2

import smbus
import time
import math
# Get I2C bus
bus = smbus.SMBus(1)

# MCP3428 address, 0x68(104)
# Send configuration command
#               0x10(16)        Continuous conversion mode, Channel-1, 12-bit Resolution
bus.write_byte(0x68, 0x18)
time.sleep(0.2)
while True:
        bus.write_byte(0x68, 0x18)
        time.sleep(0.2)
        data = bus.read_i2c_block_data(0x68,0,3)
        data[2]= data[2] >>7
        if data[2]==0:
                raw_adc = (data[0] * 256) + data[1]
                if raw_adc > 32767 :
                        raw_adc -= 65536
                current = raw_adc * 0.001390
# Output data to screen
                print "Current Values on Channel one : %.2f" %current
        time.sleep(0.2)
       
