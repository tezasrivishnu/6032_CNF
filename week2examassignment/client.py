import socket
import threading
import os, signal
s = socket.socket()
def main():
    host = "10.10.9.55"
    port = 7059
    s.connect((host,port))

    s.send(input("Input: ").encode())
    threading.Thread(target = toServer, args = ()).start()
    while True:
        message = s.recv(1024).decode()
        if message == "ATTENDANCE-SUCCESS":
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
        if not message:
            continue
    s.close()

def toServer():
    while True:
        message = input("Enter the answer:  ")
        if not message:
            continue
        s.send(message.encode())
    s.close()

if __name__ == '__main__':
    main()

