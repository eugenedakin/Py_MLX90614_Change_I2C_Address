# Py_MLX90614_Change_I2C_Address
Changes I2C address from 0x5A to 0x5C for the MLX90614 contactless thermometer using infrared radiation, on a Raspberry Pi 4. 

This Python program for the Raspberry Pi 4 uses the GY-906 sensor on the MLX90614 module board to rewrite the default address of 0x5a (hexadecimal) to 0x5c (hexadecimal). Please ensure I2C communication protocol is enabled on the Raspberry Pi. Below is a screen grab of the running program.


Screen grab of running program on Raspberry Pi 4:
![](https://github.com/eugenedakin/Py_MLX90614_Change_I2C_Address/blob/main/ScreenGrab.png)

Installation instructions:
1) Install Raspberry Pi OS (64-bit)
2) Open a terminal and type the following commands:
3) pip3 install smbus2
4) sudo apt install -y libi2c-dev i2c-tools
5) sudo apt install gpiod libgpiod-dev
6) Make sure the MLX90614 is detected at 0x5A using: i2cdetect -y 1
7) Download the python program and run with the following command `python3 I2c-MLX90614-Change-Address.py'
8) Reboot the Raspberry Pi
9) Rerun `i2cdetect -y 1`, and you should see the device populate the address at grid point 5c instead of 5a.
