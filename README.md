# OpcUaDemoServer

This is a demo server, to be used in tandem with "OpcUaDemo" project.

Server is written in python. It uses...

Typically you would install this to a VM in the cloud. The VM needs Python installed, and "pip install opcua" needs to be run. Then the real server can be started with "python server.py". It starts the OPC UA server on the VM on port 4840 (default). Typically this port needs to be enabled on your VM firewall. Use the "OpcUaDemo" project to connect to the server endpoint. You can also use any other client for the connection. 
