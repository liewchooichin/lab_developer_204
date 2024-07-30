import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cosmoslab204.documents.azure.com:443/'),
    'master_key': os.environ.get('AUTH_ACCOUNT_KEY', ""),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}