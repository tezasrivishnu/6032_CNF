import socket
import threading
import os, signal
s = socket.socket()
def main():
    host = '10.1.132.25'
    port = 7025
    s.connect((host, port))
    servermes = s.recv(1024).decode()
    print(servermes)
    s.send(input().encode())
    threading.Thread(target = toServer, args = ()).start()
    while True:
        try:
            message = s.recv(1024).decode()
            print(message)
            if message == "You successfully exited your chat,Thank you ! ":
                os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            if not message:
                continue
        except:
            print("Server Closed")
            break
    s.close()
def toServer():
    while True:
        message = input("Enter your message: ")
        if not message:
            continue
        s.send(message.encode())
    s.close()

if __name__ == '__main__':
    main()