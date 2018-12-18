import socket

def main():
    host = '10.2.138.107'
    port = 7008

    s = socket.socket()
    s.connect((host,port))

    message = input("-->")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("received from server: " + str(data))
        message = input("-->")
    s.close()
if __name__ == '__main__':
    main()