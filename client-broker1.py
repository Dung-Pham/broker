import paho.mqtt.client as mqtt

BROKER_ADDRESS = "192.168.1.52"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    publish_message("dev001/data/air", "123")
    publish_message("dev001/data/light", "456")
    publish_message("dev001/data/rain", "789")

def on_message(client, userdata, message):
    print(f"Message received on {message.topic}: {message.payload.decode()}")

def publish_message(topic, message):
    client.publish(topic, message)
    print(f"Message published to {topic}: {message}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, PORT)
client.subscribe("dev001/led")  
client.subscribe("dev001/toggle") 
print("hihi")
client.loop_forever()
