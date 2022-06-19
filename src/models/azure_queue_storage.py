from azure.storage.queue import (
    QueueClient,
    BinaryBase64EncodePolicy,
    BinaryBase64DecodePolicy
)

import os
import uuid

from dotenv import load_dotenv

load_dotenv()


class AzureQueueStorage(object):

    def __init__(self):
        # Retrieve the connection string from an environment
        # variable named AZURE_STORAGE_CONNECTION_STRING
        self.connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.queue_client = self.queue_client()
        self.create_queue()

    @classmethod
    def _generate_uuid4(cls):
        """ Create a unique name for the queue """
        return "queue-" + str(uuid.uuid4())

    def queue_client(self):
        q_name = self._generate_uuid4()

        # Instantiate a QueueClient object which will
        # be used to create and manipulate the queue
        print("Creating queue: " + q_name)
        return QueueClient.from_connection_string(self.connect_str, q_name)

    def create_queue(self):
        """ Create the queue """

        self.queue_client.create_queue()

    def send_message(self, message=u"Hello World", time_to_live=60) -> None:
        """ Queue Send message

        :param message: send message
        :param time_to_live: Specifies the time-to-live interval for the message, in seconds
        """
        print("Adding message: " + message)
        self.queue_client.send_message(message, time_to_live=time_to_live)

    def peek_messages(self):
        # Peek at the first message
        messages = self.queue_client.peek_messages()

        for peeked_message in messages:
            print("Peeked message: " + peeked_message.content)
