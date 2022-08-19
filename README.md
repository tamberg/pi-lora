# Pi LoRa
Investigating Raspberry Pi based LoRaWAN nodes, work in progress.

Initiated by Michel of [Lug Limbe](https://sokolo.cronopios.org/) ([Map](https://www.openstreetmap.org/search?query=limbe%20linux#map=19/4.01908/9.17187)).

## Overview
<img src="overview.png" width="640" />

One or more Pi LoRa devices send data to a LoRa gateway, using LoRa long range radio.

The LoRa gateway forwards received data packets to the TTN server, a LoRa cloud backend.

Any Internet-connected client computer, e.g. a Pi or laptop, can get the data from the backend.

# Pi with RN2483
We use a Pi with a RN2483 LoRa module as our LoRaWAN device.

## Wire the RN2483
Based on https://pinout.xyz/pinout/uart

<img src="rn2483-wiring.png" width="540" />

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

## Install pip3
    $ sudo apt-get update
    $ sudo apt-get install python3-pip

## Install libraries
    $ pip3 install wiringpi

## Enable UART
    $ sudo nano /boot/config.txt
    enable_uart=1
    $ sudo raspi-config # > Interface Options > Serial Port > 
        Login shell ...: No > 
        Serial port ...: Yes
    $ sudo reboot

## Configure the TTN backend
This section shows the steps to configure the TheThingsNetwork (TTN) backend.

### Register as a TTN user (once)
- https://www.thethingsnetwork.org/

### Open the TTN console
- https://eu1.cloud.thethings.network/console/

### Create an application
An application is needed per type of LoRaWAN device you want to connect, e.g. temperature sensor devices.

- Create App

### Register a device
A separate device is needed for each physical LoRaWAN device you want to connect, e.g. sensor-1 and sensor-2.

- End devices
- Add end device
- Try manual device registration
- Frequency plan: Europe (recommended)
- LoRaWAN Version: 1.0.3
- Show advanced activation
- Activation by personalisation (ABP)
- Device Address: click icon to generate
- AppSKey: click icon to generate
- NwkSKey: click icon to generate
- End device ID: pi-lora-device-0
- Register end device

### Allow frame counter reset
- General settings
- Network layer > Expand
- Advanced MAC settings
- Reset frame counter [x]
- Save changes

### Get ABP keys
- Overview
- Device Address
- AppSKey: click icon to show key
- NwkSKey: click icon to show key


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
This command line program can run on a Pi or any other computer.

## Install npm
    $ sudo apt-get install npm
## Install mqtt
    $ sudo npm install mqtt -g # adds tool to path
## Subscribe to data from TTN backend with CLI
    $ mqtt sub -t "v3/<AppID>@ttn/devices/<DevID>/up"\
    -h "eu1.cloud.thethings.network" -u "<AppID>@ttn"\
    -P "<ApiKey>" # see TTN console

# Python TTN MQTT client
This Python program can run on a Pi or any other computer.

## Install libraries
    $ pip3 install paho-mqtt
    $ pip3 install pybase64

## Download code
    $ wget https://raw.githubusercontent.com/tamberg/pi-lora/main/ttn-client.py
    $ cat ttn-client.py

## Run code
    $ python3 ttn-client

# Gateway
> Note: This section is for LoRaWAN gateways only

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
## Raspberry Pi Zero W Setup
- https://github.com/tamberg/fhnw-iot/wiki/Raspberry-Pi-Zero-W
## Raspberry Pi UART
- https://pinout.xyz/pinout/uart
- https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/computers/configuration/uart.adoc
## RN2483
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#wiring (Wiring)
- https://github.com/rac2030/MakeZurich/wiki/Using-the-Microchip-RN2483-via-Serial-to-USB#python (Code)
- https://pinboard.in/search/u:tamberg?query=rn2483 (more)
## Gateway
- https://github.com/ttn-zh/ic880a-gateway/tree/spi
## Frequencies
- https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/
- https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/
