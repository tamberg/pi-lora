# Pi LoRa
Investigating Raspberry Pi based LoRaWAN nodes, work in progress.

Initiated by Michel of [Lug Limbe](https://sokolo.cronopios.org/) ([Map](https://www.openstreetmap.org/search?query=limbe%20linux#map=19/4.01908/9.17187)).

# Wire the RN2483
Based on https://pinout.xyz/pinout/uart

Raspberry Pi|RN2483
:---|:---
RX|TX
TX|RX
RTS|CTS
CTS|RTS
-|(RST)
3V3|3V3
-|(NC)
GND|GND

# Install wiringpi
    $ pip3 install wiringpi

# Enable UART
    $ sudo nano /boot/config.txt
    enable_uart=1
    $ sudo raspi-config # > Interface Options > Serial Port > ... login shell ... No > ... serial port ... Yes
    $ sudo reboot

# Get keys from TTN
...
https://eu1.cloud.thethings.network/console/applications/pi-lora-app/devices/pi-lora-device-0

# Download code
    $ wget https://raw.githubusercontent.com/tamberg/pi-lora/main/rn2483.py
    $ cat rn2483.py

# Set keys in code
    $ nano rn2483.py
    TTN_DEV_ADDR = "00000000" # TODO
    TTN_NWK_S_KEY = "00000000000000000000000000000000" # TODO
    TTN_APP_S_KEY = "00000000000000000000000000000000" # TODO

# Run code
    $ python3 rn2483.py

# Resources
## Raspberry Pi UART Pinout
- https://pinout.xyz/pinout/uart
## RN2483
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#wiring (Wiring)
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#python (Code)
- https://pinboard.in/search/u:tamberg?query=rn2483 (more)
## Gateway
- https://github.com/ttn-zh/ic880a-gateway/tree/spi
