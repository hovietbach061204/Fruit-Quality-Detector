import azure.functions as func
import datetime
import json
import logging
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult
CONNECTION_STRING = "HostName=fruit-quality-detector-hovietbach061204.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=Ar61QMt2RSXAjRv81/YCM8z/no+swRDBcAIoTLX3Ie8="
DEVICE_ID = "camera"


# Details of the direct method to call.
METHOD_NAME = "img_capture"
METHOD_PAYLOAD = ""

app = func.FunctionApp()


@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="distance-trigger",
                               connection="EventHubConnectionString") 
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                azeventhub.get_body().decode('utf-8'))
    event_body = json.loads(azeventhub.get_body().decode('utf-8'))
    logging.info("distance = %d", event_body.get("distance", -1))
    distance = event_body.get("distance", -1)
    if distance != -1 and distance < 10:
        # send command to capture image
        logging.info("send message to device")
         # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        # Call the direct method.
        deviceMethod = CloudToDeviceMethod(method_name=METHOD_NAME, payload=METHOD_PAYLOAD)
        response = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)

        
        
        
        
        
        
        



# @app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="fruit-type",
#                                connection="EventHubConnectionString") 
# def fruit_type(azeventhub: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                 azeventhub.get_body().decode('utf-8'))
