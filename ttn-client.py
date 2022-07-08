import paho.mqtt.client as mqtt
import json
import base64

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("v3/pi-lora-app@ttn/devices/pi-lora-device-0/up")

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    json_payload = json.loads(msg.payload.decode())
    uplink_message = json_payload['uplink_message']
    frm_payload = uplink_message['frm_payload']
    lora_payload = base64.b64decode(frm_payload)
    print(lora_payload) # .decode() for strings, TODO for int

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("pi-lora-app@ttn", "TTN_PI_LORA_APP_API_KEY")
client.connect("eu1.cloud.thethings.network", 1883, 60)
client.loop_forever()
