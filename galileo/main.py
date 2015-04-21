#!/usr/bin/python
import mosquitto
import serial
import time

serialdev = '/dev/ttyACM0'

MQTT_port = 1883
MQTT_broker = "localhost"
global ser
ser = serial.Serial(serialdev, 9600, timeout=20)


def read_line():
    line = ""
    new_c = ""
    while "\n" != new_c:
        try:
            new_c = ser.read(1)
            line += new_c
        except:
            line = ""
            new_c = ""
            ser.close()
            while 1:
                time.sleep(5)
                try:
                    global ser
                    ser = serial.Serial(serialdev, 9600, timeout=20)
                    break
                except:
                    pass
    return line


def main():
    ser.flushInput()
    client_uniq = "test"
    mqttc = mosquitto.Mosquitto(client_uniq)
    mqttc.connect(MQTT_broker, MQTT_port, 60)
    while 1:
        line = read_line()
        element = line.split(" ")
        if element[0] == "dht":
            mqttc.publish("sensor/temp", element[3])
            mqttc.publish("sensor/hum", element[2])
        else:
            mqttc.publish("sensor/pres", element[1])
    mqttc.disconnect()
    ser.close()


if __name__ == '__main__':
    main()
