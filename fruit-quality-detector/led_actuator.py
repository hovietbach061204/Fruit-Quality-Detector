from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.adc import ADC
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

connection_string = 'HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0='

adc = ADC()
led = GroveLed(5)

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

def handle_method_request(request):
    print("Direct method received - ", request.name)
    
    if request.name == "led_on":
        led.on()
    elif request.name == "led_off":
        led.off()

    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

device_client.on_method_request_received = handle_method_request

while True:
    soil_moisture = adc.read(0)
    print("Soil moisture:", soil_moisture)

    message = Message(json.dumps({ 'soil_moisture': soil_moisture }))
    device_client.send_message(message)

    time.sleep(10)
    

  
    
    
    
    



# import time
# from counterfit_connection import CounterFitConnection
# from counterfit_shims_grove.grove_led import GroveLed

# from azure.iot.device import IoTHubDeviceClient, MethodResponse


# CounterFitConnection.init('127.0.0.1', 5005)

# red_led = GroveLed(1)
# green_led = GroveLed(2)

# connection_string = 'HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0='

# device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# print('Connecting')
# device_client.connect()
# print('Connected')

# def handle_method_request(request):
    
#     if request.name == "red_led_on":
#         print("Direct method received - ", request.name)
#         red_led.on()
#         green_led.off()
#     if request.name == "green_led_on":
#         print("Direct method received - ", request.name)
#         red_led.off()
#         green_led.on()

#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)

# device_client.on_method_request_received = handle_method_request

# while True:
#     time.sleep(5)
    
