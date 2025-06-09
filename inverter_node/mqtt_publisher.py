import paho.mqtt.client as mqtt
import time
import ssl

client = mqtt.Client()
client.tls_set(
    ca_certs="config/mqtt_ca.crt",
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.username_pw_set("inverter_user", "invPass123")
client.connect("control_server", 8883, 60)

try:
    while True:
        payload = "voltage=230;current=5;power=1150"
        client.publish("inverter/telemetry", payload)
        print(f"Published: {payload}")
        time.sleep(5)
except KeyboardInterrupt:
    client.disconnect()
