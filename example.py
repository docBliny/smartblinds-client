#!/usr/bin/env python3
from smartblinds_client import SmartBlindsClient
import json
import os

# Sign in with credentials in environment variables
client = SmartBlindsClient(username=os.environ.get(
    'MSB_USERNAME'), password=os.environ.get('MSB_PASSWORD'))
client.login()

# Get and print the GraphQL schema
# schema = client.get_schema()
# print(json.dumps(schema, indent=2))

# Get and print all the blinds and rooms
blinds, rooms = client.get_blinds_and_rooms()
print(blinds)
print(rooms)
print(blinds[0].name)

# Get the state for all blinds
states = client.get_blinds_state(blinds)
if len(states) > 0:
    print(states[blinds[0].encoded_mac].position)
else:
    print("Unable to get state")

# Set the position of all blinds
# client.set_blinds_position(blinds, 100)
