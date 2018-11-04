#! /usr/bin/python
from bluetooth import *
import RPi.GPIO as GPIO
import Drivetrain
    
server_sock = BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
print("Waiting For Bluetooth Connection...")
server_sock.listen(1)
client_sock, client_info = server_sock.accept()
print("Connected with ", client_info)

connected = True
Drivetain.Data.enable(True)

while True:
    data = client_sock.recv(1024)
    print("[Received]: ", data)
    
    if data == "Disable":
        GPIO.cleanup()
        client_sock.close()
        server_sock.close()
        connected = False
        print("Disconnected")
        
    Drivetrain.Data.setData(data)



