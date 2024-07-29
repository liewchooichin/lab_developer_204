import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy
from dotenv import load_dotenv

# Queue messages are stored as text. If you want to store binary data, 
# set up Base64 encoding and decoding functions before putting a message
#  in the queue.
#
# You can configure Base64 encoding and decoding functions when creating
# the client object:
def get_base64_queue_client(credential, queue_name):
    # Setup Base64 encoding and decoding functions
    # conn_str=connect_str, 
    try:
        # Load env
        load_dotenv()
        conn_str = os.getenv("STORAGE_CONN_STR")
        base64_queue_client = QueueClient.from_connection_string(
                            conn_str=conn_str,
                            credential=credential,
                            queue_name=queue_name,
                            message_encode_policy = BinaryBase64EncodePolicy(),
                            message_decode_policy = BinaryBase64DecodePolicy()
                        )
        return base64_queue_client
    except Exception as ex:
        print("Exception: get_base64_queue_client")
        print(ex)

# create a queue
def create_a_queue(queue_name, queue_client):
    """Create a queue"""
    try:
        print("Creating queue: " + queue_name)

        # Create the queue
        queue_client.create_queue()
    except Exception as ex:
        print("Exception: create_a_queue")
        print(ex)


def add_messages_to_a_queue(queue_client, msg):
    """Add add message to a queue"""
    try:
        print("\nAdding messages to the queue...")

        # Send several messages to the queue
        q_msg = queue_client.send_message(u"First message")
        return q_msg
    
    except Exception as ex:
        print("Exception: add_messages_to_a_queue")
        print(ex)


def connect_to_queue():
    """Connect to a queue in storage account"""
    try:
        # Quickstart code goes here

        # Sample queue in storage account
        print("Azure Queue storage - Python quickstart sample")

        # Create a unique name for the queue
        queue_name = "queuesample2"

        account_url = "https://storagelab204.queue.core.windows.net"
        default_credential = DefaultAzureCredential()

        # Create the QueueClient object
        # We'll use this object to create and interact with the queue
        queue_client = QueueClient(
            account_url=account_url, 
            queue_name=queue_name ,
            credential=default_credential)
        
        # Return the references
        return queue_name, default_credential, queue_client
    
    except Exception as ex:
        print('Exception:')
        print(ex)

def peek_at_messages_in_the_queue(queue_client):
    """
    Peek at the messages in the queue by calling the peek_messages method. 
    This method retrieves one or more messages from the front of the queue 
    but doesn't alter the visibility of the message.
    """
    try:
        print("\nPeek at the messages in the queue...")

        # Peek at messages in the queue
        peeked_messages = queue_client.peek_messages(max_messages=5)

        for peeked_message in peeked_messages:
            # Display the message
            print("Message: " + peeked_message.content)
    except Exception as ex:
        print("Exception: peek_at_messages_in_the_queue")
        print(ex)

def update_message_in_a_queue(queue_client, saved_msg, updated_msg):
    """
    Update the contents of a message by calling the update_message method. This method can change a message's visibility timeout and contents. The message content must be a UTF-8 encoded string that is up to 64 KB in size. Along with the new content, pass in values from the message that was saved earlier in the code. The saved_message values identify which message to update.
    """
    try:
        print("\nUpdating a message in the queue...")

        # Update a message using the message saved when calling send_message earlier
        queue_client.update_message(saved_msg, 
                                    pop_receipt=saved_msg.pop_receipt, 
                                    content=updated_msg)
    except Exception as ex:
        print("Exception: update_message_in_a_queue")
        print(ex)


def get_queue_length(queue_client):
    """
    The get_queue_properties method returns queue properties including the approximate_message_count.
    """
    try:
        properties = queue_client.get_queue_properties()
        count = properties.approximate_message_count
        print("Message count: " + str(count))
        
    except Exception as ex:
        print("Exception: get_queue_length")
        print(ex)

def receive_messages_from_queue(queue_client):
    """
    You can download previously added messages by calling the receive_messages method.
    After downloading, the messages will be cleared from the queue.
    """
    try:
        print("\nReceiving messages from the queue...")

        # Get messages from the queue
        messages = queue_client.receive_messages(
            max_messages=20,
            visibility_timeout=600)
        for m in messages:
            print(m)

        return messages
    except Exception as ex:
        print("Exception: get_queue_length")
        print(ex)

def delete_messages_from_a_queue(queue_client, messages):
    """
    Delete messages from the queue after they're received and processed. In this case, processing is just displaying the message on the console.

    The app pauses for user input by calling input before it processes and deletes the messages. Verify in your Azure portal that the resources were created correctly, before they're deleted. Any messages not explicitly deleted eventually become visible in the queue again for another chance to process them.
    """
    try:
        print("\nPress Enter key to 'process' messages and delete them from the queue...")
        input()

        for msg_batch in messages.by_page():
                for msg in msg_batch:
                    # "Process" the message
                    print(msg.content)
                    # Let the service know we're finished with
                    # the message and it can be safely deleted.
                    queue_client.delete_message(msg)
    except Exception as ex:
        print("Exception: delete_messages_from_a_queue")
        print(ex)

def delete_a_queue(queue_client):
    """
    The following code cleans up the resources the app created by deleting the queue using the delete_queue method.
    """
    try:
        print("\nPress Enter key to delete the queue...")
        input()

        # Clean up
        print("Deleting queue...")
        queue_client.delete_queue()

        print("Done")

    except Exception as ex:
        print("Exception: delete_a_queue")
        print(ex)



def main():
    """Main"""
    queue_name, default_credential, queue_client = connect_to_queue()
    #base64_client = get_base64_queue_client(credential=default_credential, queue_name=queue_name)
    #create_a_queue(queue_name=queue_name, queue_client=queue_client)
    saved_msg = add_messages_to_a_queue(queue_client=queue_client, 
                                  msg="Greeting from zebra 1")
    update_message_in_a_queue(queue_client=queue_client, 
                              saved_msg=saved_msg,
                              updated_msg="Updated: Greeting from zebra 1")
    
    saved_msg = add_messages_to_a_queue(queue_client=queue_client, 
                                  msg="Greeting from tepia 2")
    update_message_in_a_queue(queue_client=queue_client, 
                              saved_msg=saved_msg,
                              updated_msg="Updated: Greeting from tepia 2")
    
    saved_msg = add_messages_to_a_queue(queue_client=queue_client,
                                        msg="Message from somwhere")
    update_message_in_a_queue(queue_client=queue_client, 
                              saved_msg=saved_msg,
                              updated_msg="Update: Message from somewhere")
    
    get_queue_length(queue_client=queue_client)
    peek_at_messages_in_the_queue(queue_client=queue_client)
    # After receiving messages, the messages would have already been cleared
    # in the queue.
    messages = receive_messages_from_queue(queue_client)
    delete_messages_from_a_queue(queue_client=queue_client, messages=messages)
    delete_a_queue(queue_client=queue_client)


if __name__=="__main__":
    main()