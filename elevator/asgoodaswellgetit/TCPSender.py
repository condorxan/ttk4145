from socket import *
from Message import Message
import pickle

__author__ = 'kiro'

class TCPSender:
    recipientHost = ""
    recipientPort = 5005

    def getMyIP(self):
        import socket
        return socket.gethostbyname(socket.gethostname())

    def __init__(self, ip="", port=5005):
        # Set the ip to default or given value.
        if ip=="":
            # send to self if the ip is not given.
            self.recipientHost = self.getMyIP()
        else:
            self.recipientHost = ip

        # Set the port to default or given value.
        if not port or port == 0:
                self.recipientPort = 5005
        else:
            self.recipientPort = port

        print "TCP-SENDER initialized"
        print "\t target IP:", self.recipientHost
        print "\t target port:", self.recipientPort

    def send(self, ip, message):
        try:
            #print "message:", message
            print "sendIP= " + ip

            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((ip, self.recipientPort))

            sock.send(pickle.dumps(message))

            sock.close()
        except error:
            print error
            socket.close()
            exit(1)


    def broadcast(self, message):
        print "broadcasting on tcp NOT Implemented"

# test code for running only this file.
#a = TCPSender("129.241.187.145")
#message = Message("testing")
#a.send("129.241.187.145", message)
