# Pi LoRa
Investigating Raspberry Pi based LoRaWAN nodes, work in progress.

Initiated by Michel of [Lug Limbe](https://sokolo.cronopios.org/) ([Map](https://www.openstreetmap.org/search?query=limbe%20linux#map=19/4.01908/9.17187)).

# RN2483
## Wire the RN2483
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

## Install libraries
    $ pip3 install wiringpi

## Enable UART
    $ sudo nano /boot/config.txt
    enable_uart=1
    $ sudo raspi-config # > Interface Options > Serial Port > 
        Login shell should be off: No > 
        Serial port should be on: Yes
    $ sudo reboot

## Get keys from TTN
- https://www.thethingsnetwork.org/
- https://eu1.cloud.thethings.network/console/
- Create App
- Add Device
- Use ABP
- Allow reset frame counter
- Get Keys

## Download code
    $ wget https://raw.githubusercontent.com/tamberg/pi-lora/main/rn2483.py
    $ cat rn2483.py

## Set keys in code
    $ nano rn2483.py
    TTN_DEV_ADDR = "00000000" # TODO
    TTN_NWK_S_KEY = "00000000000000000000000000000000" # TODO
    TTN_APP_S_KEY = "00000000000000000000000000000000" # TODO

## Run code
    $ python3 rn2483.py

# Command line TTN MQTT client
## Install mqtt
    $ sudo npm install mqtt -g # adds tool to path
## Subscribe to data from TTN backend with CLI
    $ mqtt sub -t "v3/<AppID>@ttn/devices/<DevID>/up"\
    -h "eu1.cloud.thethings.network" -u "<AppID>@ttn"\
    -P "<ApiKey>" # see TTN console

# Python TTN MQTT client
## Install libraries
    $ pip3 install paho-mqtt
    $ pip3 install base64

## Download code
    $ wget https://raw.githubusercontent.com/tamberg/pi-lora/main/ttn-client.py
    $ cat ttn-client.py

## Run code
    $ python3 ttn-client

# Gateway
## Enable SPI
    $ sudo raspi-config # enable SPI

## Setup ttn-gateway
    $ git clone https://github.com/ttn-zh/ic880a-gateway.git ~/ic880a-gateway
    $ cd ~/ic880a-gateway
    $ sudo ./install.sh spi

## Show config
    $ cat /opt/ttn-gateway/global_conf.json

## Show log
    $ sudo journalctl -u ttn-gateway --since="1h ago"

# Resources
## LoRaWAN with TTN
- http://www.tamberg.org/fhnw/2021/hs/IoT08LoRaWANConnectivity.pdf
- http://www.tamberg.org/fhnw/2021/hs/IoT09Dashboards.pdf
## Raspberry Pi UART Pinout
- https://pinout.xyz/pinout/uart
## RN2483
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#wiring (Wiring)
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#python (Code)
- https://pinboard.in/search/u:tamberg?query=rn2483 (more)
## Gateway
- https://github.com/ttn-zh/ic880a-gateway/tree/spi
## Frequencies
- https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/
- https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/
