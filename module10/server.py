import socket
from threading import *
import os
import signal
import time
members = {}
s = socket.socket()
def main():
    host = '10.1.132.25'
    port = 7025
    s.bind((host, port))
    s.listen(10)
    print("Server started at: "+str(host))
    while True:
        c, addr = s.accept()
        print("client entering his name at IP: "+str(addr))
        servermsg = "Welcome to the Group Chat! \nPlease enter your name: "
        c.send(servermsg.encode())
        if c not in members:
            members[c] = "user"
            Thread(target = chatRoom, args = (c, "user")).start()
        else:
            c.send("Error!!, Try again".encode())
            members.pop(c)
    s.close()

def chatRoom(c, user):
    user = c.recv(1024).decode()
    members[c] = user
    Broadcast(c, user+" joined the chat")
    try:
        while c in members:
            message = c.recv(1024).decode()
            if message == "QUIT":
                message = user+ " exited the chat"
                Broadcast(c, message)
                c.send("Successfully exited your chat".encode())
                members.pop(c)
                check()
                return 1
            else:
                message = user + ": " + message+"  "
                Broadcast(c,message)
    except:
        members.pop(c)
        c.send("Error Occured, try again".encode())

def check():
    if (active_count() == 2):
        toAll("Waiting to close the group chat, no member online.")
        time.sleep(25)
        if (active_count() == 2):
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def Broadcast(c, message):
    keys = members.keys()
    print(message)
    for connection in keys:
        if c != connection:
            connection.send(message.encode())


def toAll(message):
    message = "Admin: "+ message+ " "
    keys = members.keys()
    print(message)
    for connection in keys:
        connection.send(message.encode())



if __name__ == '__main__':
    main()