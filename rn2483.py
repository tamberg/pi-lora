# Pi Zero W with RN2483 LoRaWAN via Grove UART port, plus RST
# $ pip3 install wiringpi
# $ sudo nano /boot/config.txt
# enable_uart=1
# $ sudo raspi-config # > Interface Options > Serial Port > 
# ... login shell ... No > ... serial port ... Yes
# $ sudo reboot

import wiringpi
import time

SERIAL_PORT = "/dev/ttyS0" # Grove UART port
SERIAL_BAUD = 57600 # Default rate from spec

TTN_DEV_ADDR = "00000000" # TODO
TTN_NWK_S_KEY = "00000000000000000000000000000000" # TODO
TTN_APP_S_KEY = "00000000000000000000000000000000" # TODO

def readResult(serial):
    while not wiringpi.serialDataAvail(serial):
        time.sleep(0.01);
    while wiringpi.serialDataAvail(serial):
        ch = wiringpi.serialGetchar(serial)
        print(chr(ch), end="")

def sendCmd(serial, cmd):
    print(cmd)
    wiringpi.serialPrintf(serial, cmd + "\r\n")
    readResult(serial)

def sendCmd2(serial, cmd):
    sendCmd(serial, cmd)
    readResult(serial)

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 1) # Use GPIO pin 2 as OUTPUT
wiringpi.digitalWrite(21, 1) # Set GPIO pin 2 to HIGH
wiringpi.digitalWrite(21, 0) # Set GPIO pin 2 to LOW
time.sleep(0.5)
wiringpi.digitalWrite(21, 1) # Set GPIO pin 2 to HIGH

serial = wiringpi.serialOpen(SERIAL_PORT, SERIAL_BAUD)

sendCmd(serial, "sys get ver")
sendCmd(serial, "sys get hweui")
sendCmd(serial, "mac reset 868")
sendCmd(serial, "mac set nwkskey {0}".format(TTN_NWK_S_KEY))
sendCmd(serial, "mac set appskey {0}".format(TTN_APP_S_KEY))
sendCmd(serial, "mac set devaddr {0}".format(TTN_DEV_ADDR))
sendCmd(serial, "mac set adr off")
sendCmd(serial, "mac set ar off")
sendCmd(serial, "mac set pwridx 1")
sendCmd(serial, "mac set dr 5")
sendCmd(serial, "mac save")
sendCmd2(serial, "mac join abp")
time.sleep(1)

while True:
    data = "Hello from RN2483!"
    h = str((data.encode('utf-8').hex()))
    sendCmd2(serial, "mac tx uncnf 1 {0}".format(h))
    time.sleep(10)
