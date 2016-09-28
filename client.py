# -*- coding: utf-8 -*-

import socket
import struct

s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host,port))
print(s.recv(5).decode())
inputClient =""
while inputClient!="QUT":
    inputClient = input("Que voulez vous faire?")
    s.send(inputClient.encode())
    if inputClient!="QUT":
        print(struct.unpack('f',s.recv(1200)))
    else:
        print(s.recv(1024).decode())
s.close()