# ESP8266

## Basic information on ESP8266 running micropython
* Runs mainly on two files `boot.py` and `main.py`.  
* `boot.py` runs on start up and is followed by `main.py`.  
* Programs can be transfered into the module usign `ampy` by adafruit.

## Installing firmware on the ESP8266
* Download `esptool` using `pip`  
```pip install esptool```
* Using esptool we will clear the flash of the ESP8266  
```esptool.py --port /dev/ttyUSB0 erase_flash```
* We will flash the micro-python firmware into it  
```esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20200911-v1.13.bin```
* Install `picocom` if you are on linux, with this we will get the python REPL over the serial port.  
```picocom /dev/ttyUSB0 -b115200```  
change the port (/dev/ttyUSB0) accordingly.  

Refer to the official documentation found [here](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) for more information.

## Installing and using ampy
* Downlaod ampy using `pip`.  
`pip install adafruit-ampy`
* `ampy --help` should provide all the information on how to use this tool.
* Refer this [page](https://github.com/scientifichackers/ampy) for more information.
