import azure.functions as func
import logging
from azure.iot.hub import IoTHubRegistryManager, models
import json
from azure.iot.hub import IoTHubRegistryManager, CloudToDeviceMethod
import datetime


METHOD_NAME = "led_on"  # Method name to turn LED on
METHOD_PAYLOAD = '{"name": "led_on"}'  # Payload to send for turning LED on
CONNECTION_STRING = "HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=Ar61QMt2RSXAjRv81/YCM8z/no+swRDBcAIoTLX3Ie8="
DEVICE_ID = "led"

 
app = func.FunctionApp()

@app.event_hub_trigger(event_hub_name="camera-trigger", connection="EventHubConnectionString") 
def eventhub_trigger(event: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s', event.get_body().decode('utf-8'))
    
    # Assuming the event body contains the highest probability from the camera
    highest_probability_message = event.get_body().decode('utf-8')
    # highest_probability = json.loads(highest_probability_message)["highest_probability"]
    highest_probability =  json.loads(highest_probability_message).get("highest_probability", -1)
    if highest_probability == -1:
        return
    # Create IoTHubRegistryManager
    registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

    # Trigger LED based on the highest probability received
    if highest_probability > 0.5:  # Adjust this threshold as needed
        # Turn on the LED if highest probability is above a certain threshold
        logging.info("Turning LED on")
        device_method = CloudToDeviceMethod(method_name="led_on")
        response = registry_manager.invoke_device_method(DEVICE_ID, device_method)
    else:
        # Turn off the LED if highest probability is below the threshold
        logging.info("Turning LED off")
        device_method = CloudToDeviceMethod(method_name="led_off")
        response = registry_manager.invoke_device_method(DEVICE_ID, device_method)







# METHOD_NAME = "led_on"  # Method name to turn LED on
# METHOD_PAYLOAD = '{"name": "led_on"}'  # Payload to send for turning LED on
# CONNECTION_STRING = "HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=Ar61QMt2RSXAjRv81/YCM8z/no+swRDBcAIoTLX3Ie8="
# DEVICE_ID = "led"


# app = func.FunctionApp()

# @app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="camera-trigger",
#                                connection="EventHubConnectionString") 
# def eventhub_trigger(azeventhub: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                 azeventhub.get_body().decode('utf-8'))
    
#     # Assuming the event body contains the highest probability from the camera
#     highest_probability_message = azeventhub.get_body().decode('utf-8')
#     highest_probability = json.loads(highest_probability_message)["highest_probability"]
    
#     # Trigger LED based on the highest probability received
#     if highest_probability > 0.5:  # Adjust this threshold as needed
#         # Turn on the LED if highest probability is above a certain threshold
#         logging.info("Turning LED on")
#         # Create IoTHubRegistryManager
#         registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
#         deviceMethod = CloudToDeviceMethod(method_name=METHOD_NAME, payload=METHOD_PAYLOAD)
#         response = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)
#     else:
#         # Turn off the LED if highest probability is below the threshold
#         logging.info("Turning LED off")
#         deviceMethod = CloudToDeviceMethod(method_name="led_off")
#         response = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)




# import azure.functions as func
# import datetime
# import json
# import logging
# from azure.iot.hub import IoTHubRegistryManager
# from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult
# CONNECTION_STRING = "HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=Ar61QMt2RSXAjRv81/YCM8z/no+swRDBcAIoTLX3Ie8="
# DEVICE_ID = "led"

# # Details of the direct method to call.
# METHOD_NAME = "led_on"
# METHOD_PAYLOAD = ""
# app = func.FunctionApp()


# @app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="camera-trigger",
#                                connection="EventHubConnectionString") 
# def fruit_trigger(azeventhub: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                 azeventhub.get_body().decode('utf-8'))




# import azure.functions as func
# import datetime
# import json
# import logging
# from azure.iot.hub import IoTHubRegistryManager
# from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult
# # function_app.py
# CONNECTION_STRING = "HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;DeviceId=led;SharedAccessKey=BLFwLdAmGhpS1Lgb47z2wrSmIt16KGLAPAIoTCoS3X0="
# DEVICE_ID_LED = "led"

# METHOD_NAME = "led_on"
# METHOD_PAYLOAD = ""

# app = func.FunctionApp()

# @app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="classification-trigger",
#                                connection="EventHubConnectionString") 
# def classification_trigger(azeventhub: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                 azeventhub.get_body().decode('utf-8'))
#     event_body = json.loads(azeventhub.get_body().decode('utf-8'))
#     classification = event_body.get("classification", "")
#     if classification:
#         # send command to turn LED on or off
#         logging.info("send message to device")
#         registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

#         if classification in ['Unripe tomatoes', 'Rotten tomatoes']:
#             method_name = "led_on"
#         elif classification == 'Ripe tomatoes':
#             method_name = "led_off"
#         else:
#             return

#         deviceMethod = CloudToDeviceMethod(method_name=METHOD_NAME, payload=METHOD_PAYLOAD)
#         response = registry_manager.invoke_device_method(DEVICE_ID_LED, deviceMethod)







# import logging

# from azure.functions import EventHubEvent
# from typing import List
# import json
# import os
# from azure.iot.hub import IoTHubRegistryManager
# from azure.iot.hub.models import CloudToDeviceMethod


# def run_camera(distance):
#      if distance < 50:
#             direct_method = CloudToDeviceMethod(method_name='camera_on', payload='{}')
#             registry_manager_connection_string = os.environ['REGISTRY_MANAGER_CONNECTION_STRING']
#             registry_manager = IoTHubRegistryManager(registry_manager_connection_string)
#             camera_device_id='camera-sensor-allawy'
#             registry_manager.invoke_device_method(camera_device_id, direct_method)

#             logging.info('Direct method request sent! to {camera_device_id}')

# def run_actuator(food_predictions):
#      Unripe_value = float(food_predictions["Unripte tomatoes"])
#      Ripe_value = float(food_predictions["Ripe tomatoes"])
#      Rotten_value = float(food_predictions["Rotten tomatoes"])
#      if Unripe_value > Ripe_value:
#             direct_method = CloudToDeviceMethod(method_name='red_led_on', payload='{}')
#      elif Rotten_value > Ripe_value:
#              direct_method = CloudToDeviceMethod(method_name='red_led_on', payload='{}')
#      else :
#           direct_method = CloudToDeviceMethod(method_name='green_led_on', payload='{}')
#      registry_manager_connection_string = os.environ['REGISTRY_MANAGER_CONNECTION_STRING']
#      registry_manager = IoTHubRegistryManager(registry_manager_connection_string)
#      actuator_device_id='acuator-allawy'
#      registry_manager.invoke_device_method(actuator_device_id, direct_method)

#      logging.info('Direct method request sent! to {actuator_device_id}')

             
# def main(events: List[EventHubEvent]):
#     for event in events:
#         body = json.loads(event.get_body().decode('utf-8'))
#         device_id = event.iothub_metadata['connection-device-id']

#         logging.info(f'Received message: {body} from {device_id}')
        
#         if device_id=='proximity-sensor-allawy':
#             distance = body['distance']
#             run_camera(distance)
        
#         if device_id=='camera-sensor-allawy':
#             food_predictions = body['food_predictions']
#             run_actuator(food_predictions)
       