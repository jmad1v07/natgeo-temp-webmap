import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# path to blob to upload
cwd = os.getcwd()
blob_file = "mc_1000_byte_cog.tif"
upload_file_path = os.path.join(cwd, blob_file)

# Create a blob client using the local file name as the name for the blob
container_name = "baselayer"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_file)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)

