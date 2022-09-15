from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json

class ASBClient:

    def send(data):
        """Function to send data to Azure Service Bus."""

        CONNECTION_STR = "<CONNECTION STRING>"
        #Sample connection string format: Endpoint=sb://xxxx.servicebus.windows.net....
        TOPIC_NAME = "<TOPIC NAME>"
        SUBSCRIPTION_NAME = "<SUBSCRIPTION NAME>"

        servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

        with servicebus_client:
            sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)

            with sender:
                # cast object to string friendly
                str_datadict = json.dumps(data)
                message = ServiceBusMessage(str_datadict.encode('utf-8'))
                message.subject = "<SUBJECT NAME>" # Service Bus message subject.
                sender.send_messages(message)

        return "OK"