#!/usr/bin/python
import mosquitto
import time
import random

MQTT_port = 1883
MQTT_broker = "192.168.0.1"

def read_line():
    return random.randrange(200)


def main():
    client_uniq = "test"
    mqttc = mosquitto.Mosquitto(client_uniq)
    mqttc.connect(MQTT_broker, MQTT_port, 60)
    while 1:
        time.sleep(1)
        line = read_line()
        mqttc.publish("galileo/main", str(line))
    mqttc.disconnect()


if __name__ == '__main__':
    main()
