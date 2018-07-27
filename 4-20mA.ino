// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// MCP3428
// This code is designed to work with the MCP3428_I2CADC I2C Mini Module available from ControlEverything.com.
// https://store.ncd.io/shop/?fwp_product_type=4-20ma-input-output

#include <application.h>
#include <spark_wiring_i2c.h>

// MCP3428 I2C address is 0x68(104)
#define Addr 0x68

int raw_adc = 0;
void setup()
{
  // Set variable
  Particle.variable("i2cdevice", "MCP3428");
  Particle.variable("rawADC", raw_adc);

  // Initialise I2C communication as MASTER
  Wire.begin();
  // Start serial communication and set baud rate = 9600
  Serial.begin(9600);
}

void loop()
{
  unsigned int data[2];

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select configuration command
  // Continuous conversion mode, Channel-1, 16-bit resolution, gain 2
  Wire.write(0x19);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(500);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Request 2 bytes of data
  Wire.requestFrom(Addr, 2);

  // Read 2 bytes of data
  // raw_adc msb, raw_adc lsb
  if (Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data to 16-bits
  raw_adc = (data[0]) * 256 + data[1];
  if (raw_adc > 32767)
  {
    raw_adc -= 65536;
  }

  // Output data to console
  Particle.publish("Digital value on Channel-1: ", String(raw_adc));
  delay(1000);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select configuration command
  // Continuous conversion mode, Channel-2, 16-bit resolution, gain 2
  Wire.write(0x39);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(500);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Request 2 bytes of data
  Wire.requestFrom(Addr, 2);

  // Read 2 bytes of data
  // raw_adc msb, raw_adc lsb
  if (Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data to 16-bits
  raw_adc = (data[0]) * 256 + data[1];
  if (raw_adc > 32767)
  {
    raw_adc -= 65536;
  }

  // Output data to console
  Particle.publish("Digital value on Channel-2: ", String(raw_adc));
  delay(1000);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select configuration command
  // Continuous conversion mode, Channel-3, 16-bit resolution gain 2
  Wire.write(0x59);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(500);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Request 2 bytes of data
  Wire.requestFrom(Addr, 2);

  // Read 2 bytes of data
  // raw_adc msb, raw_adc lsb
  if (Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data to 16-bits
  raw_adc = (data[0]) * 256 + data[1];
  if (raw_adc > 32767)
  {
    raw_adc -= 65536;
  }

  // Output data to console
  Particle.publish("Digital value on Channel-3: ", String(raw_adc));
  delay(1000);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select configuration command
  // Continuous conversion mode, Channel-4, 16-bit resolution gain 2
  Wire.write(0x79);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(500);

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Request 2 bytes of data
  Wire.requestFrom(Addr, 2);

  // Read 2 bytes of data
  // raw_adc msb, raw_adc lsb
  if (Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data to 16-bits
  raw_adc = (data[0]) * 256 + data[1];
  if (raw_adc > 32767)
  {
    raw_adc -= 65536;
  }

  // Output data to console
  Particle.publish("Digital value on Channel-4: ", String(raw_adc));
  delay(1000);
}
