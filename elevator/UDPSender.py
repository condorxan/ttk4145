from socket import *
import time

__author__ = 'kiro'

class UDPSender:
    UDP_IP = ""
    UDP_PORT = 0

    def __init__(self, port=5005):
        # Set the ip to default or given value.
        #self.UDP_IP = "<broadcast>"
        self.UDP_IP = "127.0.0.1"

        # Set the port to default or given value.
        if not port:
            self.UDP_PORT = 5005
        else:
            self.UDP_PORT = port

        print "SENDER initialized"
        print "UDP target IP:", self.UDP_IP
        print "UDP target port:", self.UDP_PORT

    def send(self, message):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('', 0))
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        s.sendto(message, ('<broadcast>', self.UDP_PORT))

# test code for running only this file.

#a = UDPSender()
#a.send("testing")
#a.send("testing1")
#a.send("testing2")
#a.send("testing3")

