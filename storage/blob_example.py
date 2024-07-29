# BlobServiceClient: The BlobServiceClient class allows you to manipulate 
# Azure Storage resources and blob containers.
# ContainerClient: The ContainerClient class allows you to manipulate Azure
# Storage containers and their blobs.
# BlobClient: The BlobClient class allows you to manipulate Azure Storage blobs.
#
# Authenticate to Azure and authorize access to blob data
# Create a container
# Upload blobs to a container
# List the blobs in a container
# Download blobs
# Delete a container

import os, uuid, sys
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv


def authenticate_to_storage_account():
    """Authenticate using default azure credential
    Role: Storage Blob Data Contributor to read and write blob data. 
    """
    try:
        print(f"{sys._getframe(  ).f_code.co_name}")
        account_url = "https://storagelab204.blob.core.windows.net"
        default_credential = DefaultAzureCredential()

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)
        print(f"Blob account name: {blob_service_client.account_name}")
        return blob_service_client
    
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)


def create_a_container(blob_service_client):
    """
    Create a new container in your storage account by calling the create_container method on the blob_service_client object. In this example, the code appends a GUID value to the container name to ensure that it's unique.
    """
    try:
        print(f"{sys._getframe(  ).f_code.co_name}")
        # Create a unique name for the container
        container_name = str(uuid.uuid4())

        # Create the container
        container_client = \
            blob_service_client.create_container(container_name)
        
        return container_name, container_client
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)


def upload_blobs_to_a_container(blob_service_client, container_name):
    """
    Upload a blob to a container using upload_blob. The example code creates
    a text file in the local data directory to upload to the container.
    """
    try:
        print(f"{sys._getframe(  ).f_code.co_name}")
        # Create a local directory to hold blob data
        local_path = "./data"
        os.mkdir(local_path)

        # Create a file in the local data directory to upload and download
        local_file_name = str(uuid.uuid4()) + ".txt"
        upload_file_path = os.path.join(local_path, local_file_name)

        # Write text to the file
        file = open(file=upload_file_path, mode='w')
        file.write("Hello, World!")
        file.close()

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(
             container=container_name, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(file=upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)

        return local_path, local_file_name, upload_file_path
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)


def list_blobs_in_a_container(container_client):
    """
    List the blobs in the container by calling the list_blobs method. In this case, 
    only one blob has been added to the container, so the listing operation returns
    just that one blob.
    """
    try:
        print("\nListing blobs...")

        # List the blobs in the container
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("\t" + blob.name) 
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)
         

def download_blobs(blob_service_client, container_name, local_path, local_file_name):
    """
    Download the previously created blob by calling the download_blob method.
    The example code adds a suffix of "DOWNLOAD" to the file name so that you
    can see both files in local file system.
    """
    try:
        # Download the blob to a local file
        # Add 'DOWNLOAD' before the .txt extension so you can see both files in
        # the data directory
        download_file_path = os.path.join(local_path, 
                                          str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        container_client = blob_service_client.get_container_client(container= container_name) 
        print("\nDownloading blob to \n\t" + download_file_path)

        # list the blobs
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("\t" + blob.name) 
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(
                    container_client.download_blob(blob.name).readall())

        return container_client, download_file_path
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)

def delete_a_container(container_client, upload_file_path, download_file_path, local_path):
    """
    The following code cleans up the resources the app created by removing the entire container using the delete_container method. You can also delete the local files, if you like.

    The app pauses for user input by calling input() before it deletes the blob, container, and local files. Verify that the resources were created correctly before they're deleted. 
    """
    try:
        # Clean up
        print("\nPress the Enter key to begin clean up")
        input()

        print("Deleting blob container...")
        container_client.delete_container()

        # I want to keep the files
        #print("Deleting the local source and downloaded files...")
        #os.remove(upload_file_path)
        #os.remove(download_file_path)
        #os.rmdir(local_path)

        print("Done")
    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)


def main():
    """Blob storage quick start"""
    try:
        print("Azure Blob Storage Python quickstart sample")

        # Quickstart code goes here
        blob_service_client = authenticate_to_storage_account()
        container_name, container_client = create_a_container(blob_service_client)
        local_path, local_file_name, upload_file_path = \
            upload_blobs_to_a_container(blob_service_client, container_name)
        list_blobs_in_a_container(container_client)
        container_client, download_file_path = download_blobs(blob_service_client, 
                                                              container_name,
                                                              local_path, local_file_name)
        delete_a_container(container_client, upload_file_path, download_file_path, local_path)

    except Exception as ex:
        print(f"Exception: {sys._getframe(  ).f_code.co_name}")
        print(ex)


if __name__=="__main__":
    main()