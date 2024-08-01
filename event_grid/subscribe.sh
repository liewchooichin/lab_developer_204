#!/bin/sh
# Subscribe to a custom topic
# You subscribe to an Event Grid topic to tell Event Grid 
# which events you want to track and where to send those events.
# The following script grabs the needed subscription ID from your
# account and use in the creation of the event subscription.
endpoint="${mySiteURL}/api/updates"
subId=$(az account show --subscription "" | jq -r '.id')

az eventgrid event-subscription create \
    --source-resource-id "/subscriptions/$subId/resourceGroups/az204-evgrid-rg/providers/Microsoft.EventGrid/topics/$myTopicName" \
    --name az204ViewerSub \
    --endpoint $endpoint