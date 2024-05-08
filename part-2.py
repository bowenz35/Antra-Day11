from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def upload_blob(storage_connection_string, container_name, file_path, blob_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data)
        print(f"File '{file_path}' uploaded to blob container '{container_name}' as '{blob_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

storage_connection_string = ""
container_name = "test"
file_path = ""
blob_name = os.path.basename(file_path)
upload_blob(storage_connection_string, container_name, file_path, blob_name)
