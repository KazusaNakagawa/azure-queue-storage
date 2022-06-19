from src.models.azure_queue_storage import AzureQueueStorage

if __name__ == '__main__':
    aq = AzureQueueStorage()

    for idx in range(3):
        aq.send_message(message=f"{idx}: test message {idx}")

    aq.peek_messages()
