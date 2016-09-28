# -*- coding: utf-8 -*-

import socket 
from function import *
import struct

s = socket.socket()

host = socket.gethostname()
port = 12345

s.bind((host,port))

s.listen(10)

while True:
    c,addresse = s.accept()
    c.send("HELLO".encode())
    a =""
    while a!= "QUT":
        a = c.recv(1024).decode()
        if a != "QUT":
            c.send(struct.pack('f',eval(a)))
        else:
            c.send('Vous etes deconnecte pcq vous avez entrer QUT'.encode())
    c.close()


