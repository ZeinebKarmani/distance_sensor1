# More details can be found in TechToTinker.blogspot.com
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from machine import I2C
from vl53l0x import VL53L0X

I2C_bus = I2C(0, sda=Pin(21), scl=Pin(2))
tof = VL53L0X(I2C_bus)

# The following lines of code should be tested using the REPL:
# 1. To enable/start the tof:
tof.start()
# 2. To read the current tof value:

tof.read()
# 3. To disable/stop the tof:

tof.stop()

