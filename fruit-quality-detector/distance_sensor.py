from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import requests

import time
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

from counterfit_shims_rpi_vl53l0x.vl53l0x import VL53L0X

distance_sensor = VL53L0X()
distance_sensor.begin()
connection_string = 'HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=proximity;SharedAccessKey=GD+8PrbC0NJnslkqjOBHK6iMxTmf3DIwpAIoTFJqMNk='

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

while True:
    distance_sensor.wait_ready()
    distance = distance_sensor.get_distance()
    print(f'Distance = {distance} mm')
    message = Message(json.dumps({ 'distance': distance }))
    device_client.send_message(message)

    time.sleep(10)
    
    
    
    
    
    
# from counterfit_connection import CounterFitConnection
# CounterFitConnection.init('127.0.0.1', 5000)

# import time

# from counterfit_shims_rpi_vl53l0x.vl53l0x import VL53L0X

# distance_sensor = VL53L0X()
# distance_sensor.begin()

# while True:
#     distance_sensor.wait_ready()
#     print(f'Distance = {distance_sensor.get_distance()} mm')
#     time.sleep(1)   
    
    
# from counterfit_connection import CounterFitConnection
# CounterFitConnection.init('127.0.0.1', 5000)

# import time
# import json
# from counterfit_shims_rpi_vl53l0x.vl53l0x import VL53L0X

# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

# connection_string = 'HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=proximity;SharedAccessKey=GD+8PrbC0NJnslkqjOBHK6iMxTmf3DIwpAIoTFJqMNk='

# device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# print('Connecting')
# device_client.connect()
# print('Connected')



# distance_sensor = VL53L0X()
# distance_sensor.begin()

# while True:
#     if distance_sensor.wait_ready():
#         distance = distance_sensor.get_distance()
#         print(f'Distance = {distance} mm')
#         message = Message(json.dumps({ 'distance': distance }))
#         device_client.send_message(message)
#     time.sleep(10)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# def handle_method_request(request):
#     print("Direct method received - ", request.name)
    
#     if request.name == "camera":
#         image = io.BytesIO()
#         camera.capture(image, 'jpeg')
#         image.seek(0)

#         with open('image.jpg', 'wb') as image_file:
#             image_file.write(image.read())

#         prediction_url = 'http://4.145.183.146/image' #The Public IP address of the virtual machine in on Azure portal: 13.76.179.94
#         headers = {
#             'Content-Type' : 'application/octet-stream'
#         }
#         image.seek(0)
#         response = requests.post(prediction_url, headers=headers, data=image)
#         results = response.json()
#         print(results)
#     elif request.name == "led":
#         # relay.off()

#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)

# device_client.on_method_request_received = handle_method_request