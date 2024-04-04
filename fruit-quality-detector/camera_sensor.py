
# # Camera 
# from counterfit_connection import CounterFitConnection
# import requests
# CounterFitConnection.init('127.0.0.1', 5050)
# import time
# import io
# from counterfit_shims_picamera import PiCamera
# import json
# from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
# from msrest.authentication import ApiKeyCredentials
# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
# from counterfit_shims_grove.grove_led import GroveLed

# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.rotation = 0
# device_client = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=camera;SharedAccessKey=ZL+Xq7uFiNeV9ghiYaGKCINqvl7Rw/8OJAIoTNwxTg8=')

# device_client1 = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0=')

# led = GroveLed(5)
    
# def handle_method_request(request):
#     print("Direct method received - ", request.name)
    
#     if request.name == "img_capture":
#         image = io.BytesIO()
#         camera.capture(image, 'jpeg')
#         image.seek(0)

#         with open('image.jpg', 'wb') as image_file:
#             image_file.write(image.read())

#         prediction_url = 'http://40.119.239.155/image' #The Public IP address of the virtual machine in on Azure portal: 13.76.179.94
#         headers = {
#             'Content-Type' : 'application/octet-stream'
#         }
#         image.seek(0)
#         response = requests.post(prediction_url, headers=headers, data=image)
#         results = response.json()
#         # print(results)
#         for prediction in results['predictions']:
#             print(f'{prediction["tagName"]}:\t{prediction["probability"] * 100:.2f}%')
            
#         tag_names = [prediction['tagName'] for prediction in results['predictions']]
#         print("Tag names:", tag_names)
        
#         response = requests.post(prediction_url, headers=headers, data=image)
#         results = response.json()

#         max_probability = 0
#         max_probability_tag_name = None

#         for prediction in results['predictions']:
#             tag_name = prediction['tagName']
#             probability = prediction['probability'] * 100  # Probability as a percentage
            
#             if probability > max_probability:
#                 max_probability = probability
#                 max_probability_tag_name = tag_name

#         print(f'Tag with the highest probability: {max_probability_tag_name} ({max_probability:.2f}%)')

        
#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)
    
    
#     # if "Ripe tomatoes" in tag_names:
#     #             # Turn on the LED if ripe tomatoes are detected
#     #             print("Turning LED on")
#     #             led.on()
#     #         else:
#     #         # Turn off the LED if no ripe tomatoes are detected
#     #             print("Turning LED off")
#     #             led.off()
    
# device_client.on_method_request_received = handle_method_request

# def handle_method_request1(request1):
#         print("Direct method received - ", request1.name)
#         if request1.name == "led_on":
#             led.on()
#         elif request1.name == "led_off":
#             led.off()
    
#         method_response = MethodResponse.create_from_method_request(request1, 200)
#         device_client1.send_method_response(method_response)

# device_client.on_method_request_received = handle_method_request1
        
        
    

# while True:
#     time.sleep(10)
    
    



# # camera_sensor.py
# # ...
# def handle_method_request(request):
#     # ...
#     image.seek(0)
#     response = requests.post(prediction_url, headers=headers, data=image)
#     results = response.json()
#     print(results)

#     # Send a message with the classification result
#     classification = results['predictions'][0]['tagName']
#     message = Message(json.dumps({ 'classification': classification }))
#     device_client.send_message(message)

#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)
# # ...

    
    
    
# # from counterfit_connection import CounterFitConnection
# # CounterFitConnection.init('127.0.0.1', 5050)
# # import json
# # import time
# import io
# import requests
# from counterfit_shims_picamera import PiCamera
# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

# from counterfit_connection import CounterFitConnection
# import requests
# CounterFitConnection.init('127.0.0.1', 5050)
# import time
# import io
# from counterfit_shims_picamera import PiCamera
# import json

# from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
# from msrest.authentication import ApiKeyCredentials
# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.rotation = 0

# connection_string = 'HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=camera;SharedAccessKey=ZL+Xq7uFiNeV9ghiYaGKCINqvl7Rw/8OJAIoTNwxTg8='

# device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# print('Connecting')
# device_client.connect()
# print('Connected')

# def handle_method_request(request):
    
#     if request.name == "camera_on":
#         print("Direct method received - ", request.name)
#         image = io.BytesIO()
#         camera.capture(image, 'jpeg')
#         image.seek(0)

#         with open('image.jpg', 'wb') as image_file:
#             image_file.write(image.read())

#         prediction_url = ' http://20.247.207.157/image'
#         headers = {
#             'Content-Type' : 'application/octet-stream'
#         }
#         image.seek(0)
#         response = requests.post(prediction_url, headers=headers, data=image)
#         results = response.json()
#         data={
#             results["predictions"][0]["tagName"]:f'{results["predictions"][0]["probability"]*1:.2f}',
#             results["predictions"][1]["tagName"]:f'{results["predictions"][1]["probability"]*1:.2f}',
#             results["predictions"][2]["tagName"]:f'{results["predictions"][2]["probability"]*1:.2f}'
#             }
#         for prediction in results['predictions']:
#             data={prediction["tagName"]:f'{prediction["probability"] * 100.00:.2f}%'}
#             print(f'{prediction["tagName"]}:\t{prediction["probability"] * 100:.2f}%')
#         print(data)
#         message = Message(json.dumps({ 'food_predictions': data }))
#         device_client.send_message(message)
#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)


# device_client.on_method_request_received = handle_method_request

# while True:
#      time.sleep(5)


# # Camera 
# from counterfit_connection import CounterFitConnection
# import requests
# CounterFitConnection.init('127.0.0.1', 5050)
# import time
# import io
# from counterfit_shims_picamera import PiCamera
# import json
# from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
# from msrest.authentication import ApiKeyCredentials
# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
# from counterfit_shims_grove.grove_led import GroveLed


# # Camera 
# from counterfit_connection import CounterFitConnection
# import requests
# CounterFitConnection.init('127.0.0.1', 5050)
# import time
# import io
# from counterfit_shims_picamera import PiCamera
# import json
# from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
# from counterfit_shims_grove.grove_led import GroveLed


# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.rotation = 0
# device_client = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=camera;SharedAccessKey=ZL+Xq7uFiNeV9ghiYaGKCINqvl7Rw/8OJAIoTNwxTg8=')

# device_client1 = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0=')

# led = GroveLed(5)

# def handle_method_request(request):
#     print("Direct method received - ", request.name)
    
#     if request.name == "img_capture":
#         image = io.BytesIO()
#         camera.capture(image, 'jpeg')
#         image.seek(0)

#         with open('image.jpg', 'wb') as image_file:
#             image_file.write(image.read())

#         prediction_url = 'http://40.119.239.155/image' #The Public IP address of the virtual machine in on Azure portal: 13.76.179.94
#         headers = {
#             'Content-Type' : 'application/octet-stream'
#         }
        
#         image.seek(0)
#         response = requests.post(prediction_url, headers=headers, data=image)
#         results = response.json()

#         max_probability = 0
#         max_probability_tag_name = None

#         for prediction in results['predictions']:
#             tag_name = prediction['tagName']
#             probability = prediction['probability'] * 100  # Probability as a percentage
            
#             if probability > max_probability:
#                 max_probability = probability
#                 max_probability_tag_name = tag_name

#             print(f'{tag_name}:\t{probability:.2f}%')

#         print("Tag with the highest probability:", max_probability_tag_name, f'({max_probability:.2f}%)')
        
#         # Send the highest probability tag name as a message to IoT Hub
#         message_body = json.dumps({'highest_probability_tag_name': max_probability_tag_name})
#         message = Message(message_body)
#         device_client.send_message(message)
    
#     method_response = MethodResponse.create_from_method_request(request, 200)
#     device_client.send_method_response(method_response)

# device_client.on_method_request_received = handle_method_request

# while True:
#     time.sleep(10)

from counterfit_connection import CounterFitConnection
import requests
CounterFitConnection.init('127.0.0.1', 5050)
import time
import io
from counterfit_shims_picamera import PiCamera
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
from counterfit_shims_grove.grove_led import GroveLed


camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 0
device_client = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=camera;SharedAccessKey=ZL+Xq7uFiNeV9ghiYaGKCINqvl7Rw/8OJAIoTNwxTg8=')

device_client1 = IoTHubDeviceClient.create_from_connection_string('HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0=')

led = GroveLed(5)

def handle_method_request(request):
    print("Direct method received - ", request.name)
    
    if request.name == "img_capture":
        image = io.BytesIO()
        camera.capture(image, 'jpeg')
        image.seek(0)

        with open('image.jpg', 'wb') as image_file:
            image_file.write(image.read())

        prediction_url = 'http://20.24.164.222/image' #The Public IP address of the virtual machine in on Azure portal: 13.76.179.94
        headers = {
            'Content-Type' : 'application/octet-stream'
        }
        
        image.seek(0)
        response = requests.post(prediction_url, headers=headers, data=image)
        results = response.json()

        max_probability = 0
        max_probability_tag_name = None

        for prediction in results['predictions']:
            tag_name = prediction['tagName']
            probability = prediction['probability'] * 100  # Probability as a percentage
            
            if probability > max_probability:
                max_probability = probability
                max_probability_tag_name = tag_name

            print(f'{tag_name}:\t{probability:.2f}%')

        print("Tag with the highest probability:", max_probability_tag_name, f'({max_probability:.2f}%)')
        
        # Trigger LED based on tag with highest probability
        # if max_probability_tag_name == "Ripe tomatoes":
        #     # Turn on the LED if ripe tomatoes are detected
        #     print("Turning LED on")
        #     led.on()
        # else:
        #     # Turn off the LED if no ripe tomatoes are detected
        #     print("Turning LED off")
        #     led.off()
        message_body = json.dumps({'highest_probability_tag_name': max_probability_tag_name})
        message = Message(message_body)
        device_client.send_message(message)
    
    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

device_client.on_method_request_received = handle_method_request


def handle_led_method_request(request1):
    print("Direct method received - ", request1.name)
    
    if request1.name == "led_on":
        print("Turning LED on")
        led.on()
    # elif request.name == "led_off":
    #     print("Turning LED off")
    #     led.off()
    else:
        print("Turning LED off")
        led.off()
    
    method_response = MethodResponse.create_from_method_request(request1, 200)
    device_client1.send_method_response(method_response)

device_client1.on_method_request_received = handle_led_method_request

while True:
    time.sleep(10)
